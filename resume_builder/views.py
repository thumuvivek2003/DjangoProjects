from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Resume
from .forms import ResumeForm, ExperienceFormSet, EducationFormSet, SkillFormSet
from .utils import generate_pdf_reportlab, generate_pdf_weasyprint

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resume_builder/resume_list.html', {'resumes': resumes})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        experience_formset = ExperienceFormSet(request.POST)
        education_formset = EducationFormSet(request.POST)
        skill_formset = SkillFormSet(request.POST)
        
        if form.is_valid() and experience_formset.is_valid() and education_formset.is_valid() and skill_formset.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            
            experience_formset.instance = resume
            experience_formset.save()
            
            education_formset.instance = resume
            education_formset.save()
            
            skill_formset.instance = resume
            skill_formset.save()
            
            messages.success(request, 'Resume created successfully!')
            return redirect('resume_list')
    else:
        form = ResumeForm()
        experience_formset = ExperienceFormSet()
        education_formset = EducationFormSet()
        skill_formset = SkillFormSet()
    
    return render(request, 'resume_builder/resume_form.html', {
        'form': form,
        'experience_formset': experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
    })

@login_required
def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        experience_formset = ExperienceFormSet(request.POST, instance=resume)
        education_formset = EducationFormSet(request.POST, instance=resume)
        skill_formset = SkillFormSet(request.POST, instance=resume)
        
        if form.is_valid() and experience_formset.is_valid() and education_formset.is_valid() and skill_formset.is_valid():
            resume = form.save()
            experience_formset.save()
            education_formset.save()
            skill_formset.save()
            
            messages.success(request, 'Resume updated successfully!')
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)
        experience_formset = ExperienceFormSet(instance=resume)
        education_formset = EducationFormSet(instance=resume)
        skill_formset = SkillFormSet(instance=resume)
    
    return render(request, 'resume_builder/resume_form.html', {
        'form': form,
        'experience_formset': experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
        'resume': resume,
    })

@login_required
def resume_preview(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    return render(request, 'resume_builder/resume_preview.html', {'resume': resume})

@login_required
def resume_download_pdf(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    pdf_type = request.GET.get('type', 'weasyprint')
    
    if pdf_type == 'weasyprint':
        pdf_buffer = generate_pdf_weasyprint(resume)
    else:
        pdf_buffer = generate_pdf_reportlab(resume)
    
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.full_name}_resume.pdf"'
    return response

@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted successfully!')
        return redirect('resume_list')
    return render(request, 'resume_builder/resume_confirm_delete.html', {'resume': resume})