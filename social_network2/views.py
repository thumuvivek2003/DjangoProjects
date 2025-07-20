from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from .models import Profile, Post, Comment, Follow, Like
from .forms import UserRegistrationForm, ProfileForm, UserForm, PostForm, CommentForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    # Get posts from users that the current user follows + their own posts
    following_users = Follow.objects.filter(follower=request.user).values_list('followed', flat=True)
    posts = Post.objects.filter(
        Q(author__in=following_users) | Q(author=request.user)
    ).select_related('author', 'author__profile').prefetch_related('likes', 'comments')
    
    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    # Form for creating new posts
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('social_network:home')
    else:
        post_form = PostForm()
    
    context = {
        'posts': posts,
        'post_form': post_form,
        'comment_form': CommentForm(),
        'post_content_type': ContentType.objects.get_for_model(Post),
    }
    return render(request, 'social_network/home.html', context)

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(author=user).select_related('author').prefetch_related('likes', 'comments')
    
    # Check if current user is following this user
    is_following = False
    if request.user.is_authenticated and request.user != user:
        is_following = Follow.objects.filter(follower=request.user, followed=user).exists()
    
    # Get follower and following counts
    followers_count = Follow.objects.filter(followed=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    
    context = {
        'profile': profile,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_own_profile': request.user == user,
        'comment_form': CommentForm(),
    }
    return render(request, 'social_network/profile.html', context)

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('social_network:profile', username=request.user.username)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'social_network/edit_profile.html', context)

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).select_related('author', 'author__profile')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('social_network:post_detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'post_content_type': ContentType.objects.get_for_model(Post),
        'comment_content_type': ContentType.objects.get_for_model(Comment),
    }
    return render(request, 'social_network/post_detail.html', context)

@login_required
@require_POST
def follow_user(request):
    user_id = request.POST.get('user_id')
    user_to_follow = get_object_or_404(User, id=user_id)
    
    if user_to_follow == request.user:
        return JsonResponse({'status': 'error', 'message': 'You cannot follow yourself'})
    
    follow_obj, created = Follow.objects.get_or_create(
        follower=request.user,
        followed=user_to_follow
    )
    
    if created:
        status = 'followed'
        message = f'You are now following {user_to_follow.username}'
    else:
        follow_obj.delete()
        status = 'unfollowed'
        message = f'You unfollowed {user_to_follow.username}'
    
    followers_count = Follow.objects.filter(followed=user_to_follow).count()
    
    return JsonResponse({
        'status': status,
        'message': message,
        'followers_count': followers_count
    })

@login_required
@require_POST
def like_content(request):
    content_type_id = request.POST.get('content_type_id')
    object_id = request.POST.get('object_id')
    
    content_type = get_object_or_404(ContentType, id=content_type_id)
    
    like_obj, created = Like.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )
    
    if not created:
        like_obj.delete()
        status = 'unliked'
    else:
        status = 'liked'
    
    # Get updated like count
    like_count = Like.objects.filter(
        content_type=content_type,
        object_id=object_id
    ).count()
    
    return JsonResponse({
        'status': status,
        'like_count': like_count
    })

@login_required
@require_POST
def add_comment(request):
    post_id = request.POST.get('post_id')
    content = request.POST.get('content')
    
    post = get_object_or_404(Post, id=post_id)
    
    if content:
        comment = Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )
        
        return JsonResponse({
            'status': 'success',
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'author': comment.author.username,
                'created_at': comment.created_at.strftime('%b %d, %Y at %I:%M %p'),
                'author_profile_picture': comment.author.profile.profile_picture.url if comment.author.profile.profile_picture else None,
            },
            'comment_count': post.comments.count()
        })
    
    return JsonResponse({'status': 'error', 'message': 'Content cannot be empty'})

def user_search(request):
    query = request.GET.get('q')
    users = []
    
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).select_related('profile')[:10]
    
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'social_network/search.html', context)