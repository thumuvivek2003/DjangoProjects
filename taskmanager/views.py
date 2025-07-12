from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'taskmanager/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'taskmanager/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'taskmanager/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'taskmanager/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
