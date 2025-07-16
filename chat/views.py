from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from .models import Room, Message, RoomMember
from .forms import RoomCreateForm

def home(request):
    """Home page showing all available rooms"""
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'chat/home.html', {'rooms': rooms})

@login_required
def room_list(request):
    """List all rooms user can access"""
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def room_detail(request, room_name):
    """Chat room detail view"""
    room = get_object_or_404(Room, name=room_name)
    
    # Get or create room member
    room_member, created = RoomMember.objects.get_or_create(
        room=room,
        user=request.user,
        defaults={'is_online': True}
    )
    
    # Get recent messages
    messages = Message.objects.filter(room=room).order_by('-timestamp')[:50]
    messages = reversed(messages)
    
    # Get online members
    online_members = RoomMember.objects.filter(room=room, is_online=True)
    
    context = {
        'room': room,
        'messages': messages,
        'online_members': online_members,
        'room_name_json': room_name,
    }
    
    return render(request, 'chat/room_detail.html', context)

@login_required
def create_room(request):
    """Create a new chat room"""
    if request.method == 'POST':
        form = RoomCreateForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_by = request.user
            room.save()
            
            # Add creator as a member
            RoomMember.objects.create(room=room, user=request.user)
            
            messages.success(request, f'Room "{room.name}" created successfully!')
            return redirect('chat:room_detail', room_name=room.name)
    else:
        form = RoomCreateForm()
    
    return render(request, 'chat/create_room.html', {'form': form})

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('chat:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'chat/register.html', {'form': form})

@login_required
def get_room_messages(request, room_name):
    """API endpoint to get room messages"""
    room = get_object_or_404(Room, name=room_name)
    messages = Message.objects.filter(room=room).order_by('-timestamp')[:20]
    
    messages_data = []
    for message in reversed(messages):
        messages_data.append({
            'user': message.user.username,
            'content': message.content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return JsonResponse({'messages': messages_data})