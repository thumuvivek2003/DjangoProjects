from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import Job, JobApplication, Company, UserProfile, JobCategory
from .forms import JobForm, JobApplicationForm, CompanyForm, UserProfileForm, CustomUserCreationForm

def job_list(request):
    jobs = Job.objects.filter(is_active=True).select_related('company', 'category')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) | 
            Q(company__name__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        jobs = jobs.filter(category_id=category_id)
    
    # Filter by job type
    job_type = request.GET.get('job_type')
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    
    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = JobCategory.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_job_type': job_type,
    }
    return render(request, 'jobboard/job_list.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    user_has_applied = False
    
    if request.user.is_authenticated:
        user_has_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
    
    context = {
        'job': job,
        'user_has_applied': user_has_applied,
    }
    return render(request, 'jobboard/job_detail.html', context)

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if user already applied
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=pk)
    
    # Check if deadline has passed
    if job.is_deadline_passed():
        messages.error(request, 'Application deadline has passed.')
        return redirect('job_detail', pk=pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f'New job application for {job.title}',
                    message=f'{request.user.first_name} {request.user.last_name} has applied for {job.title}.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[job.created_by.email],
                    fail_silently=True,
                )
            except:
                pass
            
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_detail', pk=pk)
    else:
        form = JobApplicationForm()
    
    return render(request, 'jobboard/apply_job.html', {'form': form, 'job': job})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    
    return render(request, 'jobboard/post_job.html', {'form': form})

@login_required
def my_jobs(request):
    jobs = Job.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'jobboard/my_jobs.html', {'jobs': jobs})

@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(applicant=request.user).order_by('-applied_at')
    return render(request, 'jobboard/my_applications.html', {'applications': applications})

@login_required
def job_applications(request, pk):
    job = get_object_or_404(Job, pk=pk, created_by=request.user)
    applications = JobApplication.objects.filter(job=job).order_by('-applied_at')
    return render(request, 'jobboard/job_applications.html', {'job': job, 'applications': applications})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('job_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'jobboard/profile.html', {'form': form, 'profile': profile})