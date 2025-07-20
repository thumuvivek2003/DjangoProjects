Hi, i am learning django with project based , so currently I want to learn | 1  | Hello Django            | Basic "Hello World" app               | Django installation, settings, runserver             | as I am beginnner please give me full code regarding above and guide me with the steps please with project name projects 


Great! Since you're just starting with Django, a **"Hello World"** app is a perfect first step. Let's walk through this **step-by-step**, using a project name: `projects`.

---

## ✅ What You’ll Learn

* Install Django
* Create a Django project called `projects`
* Create a Django app called `hello`
* Display "Hello, Django!" in the browser
* Run the development server

---

## 🧰 Prerequisites

Make sure you have **Python** installed (version 3.8+ is good). You can check with:

```bash
python3 --version
```

You’ll also need `pip` (Python package installer):

```bash
pip --version
```

---

## 🪜 Step-by-Step Guide

### **Step 1: Create a Virtual Environment**

```bash
mkdir django_projects
cd django_projects
python3 -m venv env
source env/bin/activate
```

---

### **Step 2: Install Django**

```bash
pip install django
```

---

### **Step 3: Create a New Django Project named `projects`**

```bash
django-admin startproject projects .
```

Your folder structure should look like:

```
django_projects/
├── env/
├── manage.py
└── projects/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

### **Step 4: Create a New App called `hello`**

```bash
python manage.py startapp hello
```

Now structure will be:

```
hello/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── ...
```

---

### **Step 5: Add the App to Project Settings**

Open `projects/settings.py`, find `INSTALLED_APPS`, and add `'hello',` like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',  # 👈 Add this line
]
```

---

### **Step 6: Create a Simple View**

Open `hello/views.py` and write:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, Django!")
```

---

### **Step 7: Create URL Configuration for the App**

1. In the `hello/` folder, create a file called `urls.py`.

```bash
touch hello/urls.py
```

2. Then add the following code to `hello/urls.py`:

```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world),
]
```

---

### **Step 8: Hook App URLs to Project URLs**

Open `projects/urls.py` and edit it like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # 👈 This will route root URL to hello app
]
```

---

### **Step 9: Run the Development Server**

```bash
python manage.py runserver
```

Go to your browser and open:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

You should see:

```
Hello, Django!
```

---

## ✅ Summary

| Step | Description                          |
| ---- | ------------------------------------ |
| 1-2  | Virtual environment + install Django |
| 3    | Created project `projects`           |
| 4    | Created app `hello`                  |
| 5-8  | Setup views, URLs, routing           |
| 9    | Run server and test                  |

---

Would you like me to generate the full folder structure and code as a downloadable zip or just list it all here?





Hi, i am learning django with project based , so currently I want to learn | 2  | Personal Portfolio      | Static pages with templates           | Templates, URL mapping, static files                 | as I am beginnner please give me  code regarding above and guide me with the steps please with start app portfolio

Awesome! You’re now moving to your **second Django project**: a **Personal Portfolio** website. This will help you learn **templates**, **URL mapping**, and **static files**—essential building blocks for any Django project.

---

## ✅ Project Overview

| Goal                    | Description                          |
| ----------------------- | ------------------------------------ |
| Project Name            | `projects`                           |
| App Name                | `portfolio`                          |
| Features                | Static pages: Home, About, Contact   |
| Django Concepts Learned | Templates, URL mapping, static files |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes you already followed **Hello World project** setup with `projects` as your Django project.

---

### **Step 1: Create the App**

```bash
python manage.py startapp portfolio
```

---

### **Step 2: Add `portfolio` to `settings.py`**

Open `projects/settings.py` and add `'portfolio'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'portfolio',
]
```

---

### **Step 3: Create Views**

Edit `portfolio/views.py`:

```python
from django.shortcuts import render

def home_view(request):
    return render(request, 'portfolio/home.html')

def about_view(request):
    return render(request, 'portfolio/about.html')

def contact_view(request):
    return render(request, 'portfolio/contact.html')
```

---

### **Step 4: Create URL Configuration for App**

Create a new file `portfolio/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
```

---

### **Step 5: Include `portfolio.urls` in Project URLs**

Open `projects/urls.py` and modify like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Root routed to portfolio app
]
```

---

### **Step 6: Create Templates**

Create the folder `portfolio/templates/portfolio/` and three HTML files:

#### 📁 `portfolio/templates/portfolio/home.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home - Portfolio</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>Welcome to My Portfolio</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about/">About</a> |
        <a href="/contact/">Contact</a>
    </nav>
</body>
</html>
```

#### 📁 `portfolio/templates/portfolio/about.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Me</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>About Me</h1>
    <p>This is a basic portfolio page.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### 📁 `portfolio/templates/portfolio/contact.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>Contact</h1>
    <p>Email: me@example.com</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

---

### **Step 7: Setup Static Files**

1. In `settings.py`, add:

```python
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

2. Create a static directory for your app:

```bash
mkdir -p portfolio/static/portfolio
```

3. Add CSS file: `portfolio/static/portfolio/styles.css`

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 40px;
}
h1 {
    color: #333;
}
a {
    color: #007bff;
    text-decoration: none;
}
```

---

### **Step 8: Run the Server**

```bash
python manage.py runserver
```

---

### **Step 9: Visit in Browser**

* **Home:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **About:** [http://127.0.0.1:8000/about/](http://127.0.0.1:8000/about/)
* **Contact:** [http://127.0.0.1:8000/contact/](http://127.0.0.1:8000/contact/)

---

## ✅ Summary

| Feature      | Description              |
| ------------ | ------------------------ |
| Templates    | HTML pages in app folder |
| Static Files | CSS linked to HTML pages |
| URL Mapping  | `urls.py` per app        |
| Views        | `render()` returns HTML  |

---

Would you like the entire file/folder structure visualized or zipped for download?


here update according to name  in the href 
You're doing great! It looks like you're building three pages: **Home**, **About**, and **Contact**. You've provided:

1. Three HTML templates (but all pasted together).
2. A `urls.py` file with appropriate paths.
3. Now you want the setup updated so each page is correctly served using proper Django naming.

---

## ✅ Let's organize and correct everything:

---

### 📁 1. Organize Your Template Files

Ensure you have **three separate template files**:

#### `pages/templates/pages/home.html`

```html
<!DOCTYPE html>
{% load static %}
<html>
<head>
    <title>Home - Portfolio</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>Welcome to My Portfolio</h1>
    <nav>
        <a href="{% url 'home' %}">Home</a> |
        <a href="{% url 'about' %}">About</a> |
        <a href="{% url 'contact' %}">Contact</a>
    </nav>
</body>
</html>
```

#### `pages/templates/pages/about.html`

```html
<!DOCTYPE html>
{% load static %}
<html>
<head>
    <title>About Me</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>About Me</h1>
    <p>This is a basic portfolio page.</p>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
```

#### `pages/templates/pages/contact.html`

```html
<!DOCTYPE html>
{% load static %}
<html>
<head>
    <title>Contact</title>
    <link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
</head>
<body>
    <h1>Contact</h1>
    <p>Email: me@example.com</p>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
```

---

### 🧠 2. Define Views in `pages/views.py`

Make sure you have:

```python
from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')
```

---

### 🌐 3. Define URLs in `pages/urls.py`

Your code here looks great, just ensure the file structure and indentation are correct:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
```

---

### 🔗 4. Connect the app's URLs to the main project

In `portfolio_site/urls.py`, make sure you include the app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

---

### 🎨 5. Your Static Files

Your CSS file should be located at:

```
pages/static/portfolio/styles.css
```

Example content:

```css
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    padding: 40px;
}
nav a {
    margin-right: 15px;
    text-decoration: none;
    color: #333;
}
```

---

## ✅ Final Check

1. Start your server:

   ```bash
   python manage.py runserver
   ```

2. Visit:

   * `http://127.0.0.1:8000/` → Home
   * `http://127.0.0.1:8000/about/` → About
   * `http://127.0.0.1:8000/contact/` → Contact

---

Let me know if you'd like to **add a base template**, **contact form**, or **deploy** your site next!





# P3 : Blog App                | CRUD blog with posts                  | Models, Admin, Forms, Views
Hi, i am learning django with project based , so currently I want to learn | 3  | Blog App                | CRUD blog with posts                  | Models, Admin, Forms, Views                          | as I am beginnner please give me  code regarding above and guide me with the steps please with start app BlogApp 

Perfect! You're moving on to one of the **most important Django projects** for beginners: a **Blog App with CRUD functionality**. This will teach you:

* Django **Models**
* Django **Admin**
* Django **Forms**
* Django **Views (CBV/FBV)**

We'll name your app `BlogApp` and continue inside your main Django project (`projects`).

---

## ✅ Blog App Features

| Feature     | Description            |
| ----------- | ---------------------- |
| Create Post | Create a new blog post |
| Read Post   | View all blog posts    |
| Update Post | Edit a blog post       |
| Delete Post | Delete a blog post     |

---

## 🪜 Step-by-Step Setup

> ✅ Assumes Django project `projects` already exists and you're inside a virtual environment.

---

### **Step 1: Create App**

```bash
python manage.py startapp BlogApp
```

---

### **Step 2: Register App in `settings.py`**

In `projects/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'BlogApp',
]
```

---

### **Step 3: Define Model**

Open `BlogApp/models.py`:

```python
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
```

---

### **Step 4: Make Migrations & Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 5: Register Model in Admin**

In `BlogApp/admin.py`:

```python
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

Create superuser (if not already):

```bash
python manage.py createsuperuser
```

Then visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to login and test.

---

### **Step 6: Create Forms**

In `BlogApp/forms.py`:

```python
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
```

---

### **Step 7: Create Views**

In `BlogApp/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'BlogApp/blog_list.html', {'posts': posts})

def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'BlogApp/blog_form.html', {'form': form})

def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, 'BlogApp/blog_form.html', {'form': form})

def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog_list')
    return render(request, 'BlogApp/blog_confirm_delete.html', {'post': post})
```

---

### **Step 8: Create URLs**

In `BlogApp/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/edit/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]
```

In `projects/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('BlogApp.urls')),  # 👈 Add this
]
```

---

### **Step 9: Create Templates**

Inside `BlogApp/templates/BlogApp/` create the following files:

#### 📄 `blog_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <a href="{% url 'blog_create' %}">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li>
                <strong>{{ post.title }}</strong><br>
                {{ post.content|linebreaks }}<br>
                <a href="{% url 'blog_update' post.pk %}">Edit</a> |
                <a href="{% url 'blog_delete' post.pk %}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### 📄 `blog_form.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Create / Edit Blog</title>
</head>
<body>
    <h1>Create / Edit Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    <a href="{% url 'blog_list' %}">Back</a>
</body>
</html>
```

#### 📄 `blog_confirm_delete.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Blog</title>
</head>
<body>
    <h1>Delete Post</h1>
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
    </form>
    <a href="{% url 'blog_list' %}">Cancel</a>
</body>
</html>
```

---

### **Step 10: Run the Server**

```bash
python manage.py runserver
```

* **Blog List:** [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)
* **Create Post:** [http://127.0.0.1:8000/blog/create/](http://127.0.0.1:8000/blog/create/)

---

## ✅ Summary

| Feature   | Where                                    |
| --------- | ---------------------------------------- |
| Model     | `BlogPost` in `models.py`                |
| Admin     | Registered in `admin.py`                 |
| Form      | `BlogPostForm` in `forms.py`             |
| Views     | `views.py`: CRUD                         |
| URLs      | `BlogApp/urls.py` and `projects/urls.py` |
| Templates | List, form, confirm delete pages         |

---

Would you like me to generate the full folder structure visually or zip it for easier download?




# 4  | Contact Form            | Form that emails data                 | Forms, Email backend, Validation
Hi, i am learning django with project based , so currently I want to learn || 4  | Contact Form            | Form that emails data                 | Forms, Email backend, Validation                     | as I am beginnner please give me  code regarding above and guide me with the steps please with start app contactForm

Great! You're moving to **Step 4: Contact Form**, which will teach you to:

* Create Django **Forms**
* Handle **form validation**
* Send emails using Django's **email backend**

We’ll use the app name: `contactForm`.

---

## ✅ Project Overview

| Feature      | Description                       |
| ------------ | --------------------------------- |
| App Name     | `contactForm`                     |
| Input Fields | Name, Email, Message              |
| Goal         | Send email with submitted message |
| Concepts     | Forms, Validation, Email backend  |

---

## 🪜 Step-by-Step Setup

> ✅ Assumes Django project is named `projects` and you're in a virtual environment.

---

### **Step 1: Create App**

```bash
python manage.py startapp contactForm
```

---

### **Step 2: Register App**

In `projects/settings.py`, add `'contactForm',` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'contactForm',
]
```

---

### **Step 3: Create the Contact Form**

In `contactForm/forms.py`:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---

### **Step 4: Configure Email Backend in `settings.py`**

Add this to `projects/settings.py` (development only):

```python
# Email config (console backend for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'you@example.com'  # Used in the email "From" field
```

> 📢 In production, use `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'` with SMTP credentials.

---

### **Step 5: Create Views**

In `contactForm/views.py`:

```python
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=f"Contact Form from {cd['name']}",
                message=cd['message'],
                from_email=cd['email'],
                recipient_list=['your@email.com'],  # Replace with your email
            )
            submitted = True
    else:
        form = ContactForm()
    
    return render(request, 'contactForm/contact.html', {'form': form, 'submitted': submitted})
```

---

### **Step 6: Create URLs**

Create `contactForm/urls.py`:

```python
from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', contact_view, name='contact'),
]
```

And include in `projects/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contactForm.urls')),  # 👈 Add this
]
```

---

### **Step 7: Create Template**

Create folder: `contactForm/templates/contactForm/`

📄 `contact.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    {% if submitted %}
        <p>✅ Your message was sent successfully!</p>
    {% else %}
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Send</button>
        </form>
    {% endif %}
</body>
</html>
```

---

### **Step 8: Run the Server**

```bash
python manage.py runserver
```

Go to: [http://127.0.0.1:8000/contact/](http://127.0.0.1:8000/contact/)

Submit the form and check your console for the "sent" email.

---

## ✅ Summary

| Part         | Location                                         |
| ------------ | ------------------------------------------------ |
| Form         | `contactForm/forms.py`                           |
| View         | `contactForm/views.py`                           |
| URL Config   | `contactForm/urls.py`, project `urls.py`         |
| Template     | `contactForm/templates/contactForm/contact.html` |
| Email Output | Console (`EMAIL_BACKEND`)                        |

---

Would you like me to show how to test this with real email (Gmail SMTP or others), or continue to the next project step?


#  5  | Task Manager            | Create, update, delete tasks          | CBVs, CRUD, Django ORM   
Great progress! You're now on **Step 5: Task Manager**, which introduces:

* **CBVs** (Class-Based Views)
* Full **CRUD** operations
* Use of **Django ORM**

However, since this is a **Task Manager**, it's better to create a new app named: `taskmanager` (instead of reusing `contactForm`).

---

## ✅ Project Overview

| Feature  | Description                         |
| -------- | ----------------------------------- |
| App Name | `taskmanager`                       |
| Goal     | Create, view, update, delete tasks  |
| Concepts | CBVs, CRUD, ORM                     |
| Model    | Task: title, description, completed |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes Django project `projects` is already set up.

---

### **Step 1: Create App**

```bash
python manage.py startapp taskmanager
```

---

### **Step 2: Register App**

In `projects/settings.py`, add `'taskmanager'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'taskmanager',
]
```

---

### **Step 3: Create Task Model**

In `taskmanager/models.py`:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

### **Step 4: Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 5: Create URLs**

In `taskmanager/urls.py`:

```python
from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
```

In `projects/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('taskmanager.urls')),  # 👈 Add this
]
```

---

### **Step 6: Create CBVs (Class-Based Views)**

In `taskmanager/views.py`:

```python
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
```

---

### **Step 7: Create Templates**

Create directory: `taskmanager/templates/taskmanager/`

#### 📄 `task_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Tasks</title>
</head>
<body>
    <h1>Task List</h1>
    <a href="{% url 'task_create' %}">+ Add New Task</a>
    <ul>
        {% for task in tasks %}
            <li>
                <strong>{{ task.title }}</strong> - 
                {% if task.completed %}✅{% else %}❌{% endif %}<br>
                <a href="{% url 'task_edit' task.pk %}">Edit</a> | 
                <a href="{% url 'task_delete' task.pk %}">Delete</a>
            </li>
        {% empty %}
            <li>No tasks available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### 📄 `task_form.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Create / Edit Task</title>
</head>
<body>
    <h1>Create / Edit Task</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    <a href="{% url 'task_list' %}">Back</a>
</body>
</html>
```

#### 📄 `task_confirm_delete.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Task</title>
</head>
<body>
    <h1>Delete Task</h1>
    <p>Are you sure you want to delete "{{ object.title }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
    </form>
    <a href="{% url 'task_list' %}">Cancel</a>
</body>
</html>
```

---

### **Step 8: Run the Server**

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/tasks/](http://127.0.0.1:8000/tasks/)

---

## ✅ Summary

| Feature   | Location                          |
| --------- | --------------------------------- |
| Model     | `Task` in `models.py`             |
| CBVs      | `views.py`: ListView, CreateView… |
| CRUD URLs | `taskmanager/urls.py`             |
| Templates | List, Form, Confirm Delete HTML   |
| ORM Used  | For all DB interactions           |

---

Would you like to include **login/logout and user-specific tasks** next, or move on to the next project in your learning plan?




# 6  | User Auth System        | Login, Register, Logout               | `auth` module, sessions, hashing                     |
Hi, i am learning django with project based , so currently I want to learn | 6  | User Auth System        | Login, Register, Logout               | `auth` module, sessions, hashing                     | as I am beginnner please give me  code regarding above and guide me with the steps please with start app 

Excellent! You’re now diving into **User Authentication** in Django—one of the most critical features for any web app. This step teaches you:

* User **registration**
* User **login/logout**
* Django’s built-in `auth` module
* **Session management**
* Password **hashing**

---

## ✅ Project Overview

| Feature     | Description                      |
| ----------- | -------------------------------- |
| App Name    | `accounts`                       |
| Goal        | User registration, login, logout |
| Key Modules | `django.contrib.auth`            |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes you're inside a Django project (`projects`)

---

### **Step 1: Create App**

```bash
python manage.py startapp accounts
```

---

### **Step 2: Register App**

In `projects/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'accounts',
]
```

---

### **Step 3: Set Up URLs**

In `accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

In `projects/urls.py`, include:

```python
path('accounts/', include('accounts.urls')),
```

---

### **Step 4: Create Forms**

In `accounts/forms.py`:

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        cpw = cleaned_data.get("confirm_password")

        if pw != cpw:
            raise forms.ValidationError("Passwords do not match.")
```

---

### **Step 5: Create Views**

In `accounts/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            login(request, user)
            return redirect('home')  # Update this as needed
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Update this as needed
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
```

---

### **Step 6: Create Templates**

Inside `accounts/templates/accounts/`:

#### 📄 `register.html`

```html
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
<a href="{% url 'login' %}">Already have an account? Login</a>
```

#### 📄 `login.html`

```html
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Create new account</a>
```

> 💡 Optional: Add a simple `home` view/template to redirect after login/registration.

---

### **Step 7: Add Login Redirect Settings**

In `settings.py`:

```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```

---

### **Step 8: Add Home View (Optional)**

In any app (e.g., `taskmanager/views.py` or a new app):

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')
```

In `projects/urls.py`:

```python
from your_app.views import home_view
path('', home_view, name='home'),
```

Create a simple `home.html`:

```html
<h2>Welcome, {{ request.user.username }}!</h2>
<a href="{% url 'logout' %}">Logout</a>
```

---

### ✅ Final URLs Summary

| URL                   | View                    |
| --------------------- | ----------------------- |
| `/accounts/register/` | Register new user       |
| `/accounts/login/`    | Login existing user     |
| `/accounts/logout/`   | Logout current user     |
| `/`                   | Home page (after login) |

---

## ✅ Summary

| Feature   | Implemented With                    |
| --------- | ----------------------------------- |
| Register  | Custom form + Django User model     |
| Login     | Built-in `AuthenticationForm`       |
| Logout    | `logout()` function                 |
| Passwords | Hashed via `set_password()`         |
| Sessions  | Handled by Django `auth` middleware |

---

Would you like to include **email verification**, **password reset**, or **restrict views by login status** next?



# 7   | Notes App               | Notes for each user only              | ForeignKeys, user access control      
Hi, i am learning django with project based , so currently I want to learn | 7  | Notes App               | Notes for each user only              | ForeignKeys, user access control                     | as I am beginnner please give me  code regarding above and guide me with the steps please with start app 

Perfect! You're now moving to **Step 7: Notes App**, which teaches you how to:

* Link models to specific users using **ForeignKeys**
* Restrict data access to only the logged-in user
* Implement a full **CRUD** app with **user access control**

We’ll start a new app named: `notes`.

---

## ✅ Project Overview

| Feature      | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| App Name     | `notes`                                                         |
| Goal         | Each user can Create, View, Update, Delete only their own notes |
| Key Concepts | ForeignKey (User), login\_required decorators, user filtering   |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes Django project `projects` is already created and login system is working.

---

### **Step 1: Create App**

```bash
python manage.py startapp notes
```

---

### **Step 2: Register App**

In `projects/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'notes',
]
```

---

### **Step 3: Create the Model**

In `notes/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

### **Step 4: Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 5: Create Views (Class-Based Views)**

In `notes/views.py`:

```python
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
```

---

### **Step 6: Create URLs**

In `notes/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('create/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]
```

In `projects/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('notes/', include('notes.urls')),
]
```

---

### **Step 7: Create Templates**

Create the folder: `notes/templates/notes/`

#### 📄 `note_list.html`

```html
<h2>My Notes</h2>
<a href="{% url 'note_create' %}">+ Add New Note</a>
<ul>
    {% for note in notes %}
        <li>
            <strong>{{ note.title }}</strong><br>
            {{ note.content|linebreaks }}<br>
            <a href="{% url 'note_edit' note.pk %}">Edit</a> |
            <a href="{% url 'note_delete' note.pk %}">Delete</a>
        </li>
    {% empty %}
        <li>No notes yet.</li>
    {% endfor %}
</ul>
```

#### 📄 `note_form.html`

```html
<h2>Create / Edit Note</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{% url 'note_list' %}">Back</a>
```

#### 📄 `note_confirm_delete.html`

```html
<h2>Delete Note</h2>
<p>Are you sure you want to delete "{{ object.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, delete</button>
</form>
<a href="{% url 'note_list' %}">Cancel</a>
```

---

### **Step 8: Run the Server**

```bash
python manage.py runserver
```

* Go to: [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/)
* Make sure you're logged in — notes are user-specific!

---

## ✅ Summary

| Feature        | Where                                                                   |
| -------------- | ----------------------------------------------------------------------- |
| Model          | `Note` with `user = ForeignKey(User)`                                   |
| Views (CBV)    | `ListView`, `CreateView`, `UpdateView`, `DeleteView` with login control |
| Templates      | For list, form, and delete                                              |
| Data filtering | Only show notes for logged-in user                                      |

---

Would you like to extend this with **tags**, **search**, or **markdown support** next?


# Image Gallery 
Hi, i am learning django with project based , so currently I want to learn | 8  | Image Gallery           | Upload and display images             | File uploads, ImageField, media settings           | as I am beginnner please give me  code regarding above and guide me with the steps please with start app 

Great! You're now on **Step 8: Image Gallery**, which will teach you how to:

* Upload and save image files
* Use Django's `ImageField`
* Configure and serve **media files**
* Display uploaded images in templates

We'll name the app: `gallery`.

---

## ✅ Project Overview

| Feature      | Description                                          |
| ------------ | ---------------------------------------------------- |
| App Name     | `gallery`                                            |
| Goal         | Upload and view images                               |
| Key Concepts | `ImageField`, `MEDIA_ROOT`, `MEDIA_URL`, file upload |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes Django project is `projects`, you're in a virtual environment, and static/media folders are not yet configured.

---

### **Step 1: Create the App**

```bash
python manage.py startapp gallery
```

---

### **Step 2: Register the App**

In `projects/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'gallery',
]
```

---

### **Step 3: Configure Media Settings**

In `projects/settings.py`, add:

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In `projects/urls.py`, add media serving config (at the bottom):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### **Step 4: Create Model**

In `gallery/models.py`:

```python
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
```

---

### **Step 5: Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 6: Forms**

In `gallery/forms.py`:

```python
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
```

---

### **Step 7: Views**

In `gallery/views.py`:

```python
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def gallery_view(request):
    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})
```

---

### **Step 8: URLs**

In `gallery/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
]
```

In `projects/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('gallery/', include('gallery.urls')),
]
```

---

### **Step 9: Templates**

Create `gallery/templates/gallery/` directory.

#### 📄 `gallery.html`

```html
<h2>Image Gallery</h2>
<a href="{% url 'upload_image' %}">Upload New Image</a>
<hr>
{% for img in images %}
    <div>
        <h3>{{ img.title }}</h3>
        <img src="{{ img.image.url }}" width="300">
    </div>
{% empty %}
    <p>No images uploaded yet.</p>
{% endfor %}
```

#### 📄 `upload.html`

```html
<h2>Upload Image</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
<a href="{% url 'gallery' %}">Back to Gallery</a>
```

---

### **Step 10: Run the Server**

```bash
python manage.py runserver
```

Visit:

* [http://127.0.0.1:8000/gallery/](http://127.0.0.1:8000/gallery/) – See uploaded images
* [http://127.0.0.1:8000/gallery/upload/](http://127.0.0.1:8000/gallery/upload/) – Upload new image

---

### ✅ Requirements for Image Upload

Make sure you have **Pillow** installed:

```bash
pip install pillow
```

---

## ✅ Summary

| Part         | Implementation                         |
| ------------ | -------------------------------------- |
| Image Upload | `ImageField`, `request.FILES`          |
| Display      | `{{ image.image.url }}` in templates   |
| Media Files  | `MEDIA_URL`, `MEDIA_ROOT`, and routing |
| Security     | Only allowed via `POST` + CSRF token   |

---

Would you like to add **image deletion**, **user-specific galleries**, or **image resizing/thumbnails** next?


# 9 Todo API 
Hi, i am learning django with project based , so currently I want to learn | 9  | Todo API                | RESTful To-do backend                 | Django REST Framework, serializers                   | as I am beginnner please give me  code regarding above and guide me with the steps please with start app 

Awesome! You’re now stepping into **Django REST Framework (DRF)** with a **RESTful To-Do API** — a crucial skill for building backends for frontend frameworks like React or mobile apps.

---

## ✅ Project Overview

| Feature      | Description                       |
| ------------ | --------------------------------- |
| App Name     | `todoapi`                         |
| Goal         | Create a REST API for to-do items |
| Key Concepts | DRF, Serializers, API Views, CRUD |

---

## 🪜 Step-by-Step Guide

> ✅ Assumes you have a Django project (`projects`) and a virtual environment.

---

### **Step 1: Install DRF**

```bash
pip install djangorestframework
```

In `projects/settings.py`, add `'rest_framework'`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'todoapi',
]
```

---

### **Step 2: Create App**

```bash
python manage.py startapp todoapi
```

---

### **Step 3: Create the Model**

In `todoapi/models.py`:

```python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

### **Step 4: Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 5: Create Serializer**

In `todoapi/serializers.py`:

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
```

---

### **Step 6: Create API Views**

In `todoapi/views.py`:

```python
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

---

### **Step 7: Create URLs**

In `todoapi/urls.py`:

```python
from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo_detail'),
]
```

In `projects/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api/', include('todoapi.urls')),
]
```

---

### **Step 8: Run Server and Test**

```bash
python manage.py runserver
```

* 📘 List/Create Todos: [http://127.0.0.1:8000/api/todos/](http://127.0.0.1:8000/api/todos/)
* 📘 Retrieve/Update/Delete: [http://127.0.0.1:8000/api/todos/1/](http://127.0.0.1:8000/api/todos/1/)

> You can use Postman, cURL, or the built-in DRF web UI.

---

## ✅ Example JSON

### ➕ POST `/api/todos/`

```json
{
  "title": "Learn DRF",
  "completed": false
}
```

### ✔ GET `/api/todos/`

```json
[
  {
    "id": 1,
    "title": "Learn DRF",
    "completed": false
  }
]
```

---

## ✅ Summary

| Feature    | Where                                               |
| ---------- | --------------------------------------------------- |
| Model      | `todoapi/models.py`                                 |
| Serializer | `todoapi/serializers.py`                            |
| Views      | `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView` |
| URLs       | `api/todos/`, `api/todos/<pk>/`                     |
| Tools      | Django REST Framework                               |

---

Would you like to add **authentication**, **pagination**, or connect this to a **React frontend** next?


# 10 :  Weather App             | Fetch weather using API               | External APIs, requests library       
Hi, i am learning django with project based , so currently I want to learn | 10 | Weather App             | Fetch weather using API               | External APIs, requests library                      | as I am beginnner please give me  code regarding above and guide me with the steps please with start app  with api https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m  

Awesome! You're now on **Step 10: Weather App**, where you'll learn to:

* Use the `requests` library to call an **external API**
* Parse and display weather data
* Handle API requests within Django views

We'll use the app name: `weather`.

---

## ✅ API Used

**Open-Meteo API:**

```bash
https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m
```

This returns hourly temperature for **Tokyo** (`latitude=35.6895`, `longitude=139.6917`).

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Create the App**

```bash
python manage.py startapp weather
```

---

### **Step 2: Register the App**

In `projects/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'weather',
]
```

---

### **Step 3: Install `requests` Library**

If not installed:

```bash
pip install requests
```

---

### **Step 4: Create the View**

In `weather/views.py`:

```python
import requests
from django.shortcuts import render

def weather_view(request):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': 35.6895,
        'longitude': 139.6917,
        'hourly': 'temperature_2m'
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract first 12 temperature readings (for 12 hours)
    hourly_times = data['hourly']['time'][:12]
    hourly_temps = data['hourly']['temperature_2m'][:12]

    forecast = zip(hourly_times, hourly_temps)

    return render(request, 'weather/weather.html', {'forecast': forecast})
```

---

### **Step 5: Create URLs**

In `weather/urls.py`:

```python
from django.urls import path
from .views import weather_view

urlpatterns = [
    path('', weather_view, name='weather'),
]
```

And include in `projects/urls.py`:

```python
path('weather/', include('weather.urls')),
```

---

### **Step 6: Create Template**

In `weather/templates/weather/weather.html`:

```html
<h2>Tokyo Weather Forecast (Next 12 Hours)</h2>
<table border="1" cellpadding="5">
    <tr>
        <th>Time</th>
        <th>Temperature (°C)</th>
    </tr>
    {% for time, temp in forecast %}
        <tr>
            <td>{{ time }}</td>
            <td>{{ temp }}</td>
        </tr>
    {% endfor %}
</table>
```

---

### **Step 7: Run the Server**

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/weather/](http://127.0.0.1:8000/weather/)

---

## ✅ Summary

| Feature         | Location                                          |
| --------------- | ------------------------------------------------- |
| API Integration | `requests.get()` in `views.py`                    |
| API Source      | [Open-Meteo Forecast API](https://open-meteo.com) |
| View            | Weather forecast for next 12 hours                |
| Template        | Renders a simple table with results               |

---

Would you like to add **city input**, **chart display with Chart.js**, or make it support **dynamic coordinates** next?


# 11 : Polls App               | Voting and displaying results         | Relationships, Aggregation, Template logic  
Hi, i am learning django with project based , so currently I want to learn | 11 | Polls App               | Voting and displaying results         | Relationships, Aggregation, Template logic           | as I am beginnner please give me  code regarding above and guide me with the steps please with start app 



# 12 | E-commerce Base         | Product listing, cart                 | Models, ForeignKey, Template Inheritance    
Hi, i am learning django with project based , so currently I want to learn | 12 | E-commerce Base         | Product listing, cart                 | Models, ForeignKey, Template Inheritance             | as I am beginnner please give me  code regarding above and guide me with the steps please with start app  with full code please

Great! Let’s build a basic **E-commerce app** in Django with:

* Product Listing
* Cart System
* Models with ForeignKey
* Template Inheritance

We’ll do this in a new Django app named `shop`.

---

### ✅ Step-by-step Setup

---

### 1. **Create Django Project (if not done)**

```bash
django-admin startproject ecommerce_project
cd ecommerce_project
python manage.py startapp shop
```

---

### 2. **Add `shop` to `INSTALLED_APPS` in `settings.py`**

```python
INSTALLED_APPS = [
    ...
    'shop',
]
```

---

### 3. **Create Models in `shop/models.py`**

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
```

---

### 4. **Migrate and Create Superuser**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### 5. **Register Models in `shop/admin.py`**

```python
from django.contrib import admin
from .models import Product, Cart, CartItem

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
```

---

### 6. **Add Media Settings in `settings.py`**

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In `urls.py` of main project:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 7. **Create Views in `shop/views.py`**

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(id=1)  # For now, single cart
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

def view_cart(request):
    cart = Cart.objects.get(id=1)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'items': items})
```

---

### 8. **Configure URLs in `shop/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]
```

In main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]
```

---

### 9. **Templates with Inheritance**

`shop/templates/shop/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>My E-commerce</title>
</head>
<body>
    <h1>Welcome to My E-commerce</h1>
    <a href="{% url 'product_list' %}">Products</a> | 
    <a href="{% url 'view_cart' %}">Cart</a>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

`shop/templates/shop/product_list.html`

```html
{% extends 'shop/base.html' %}

{% block content %}
<h2>Products</h2>
{% for product in products %}
    <div>
        <img src="{{ product.image.url }}" height="100">
        <p>{{ product.name }} - ₹{{ product.price }}</p>
        <p>{{ product.description }}</p>
        <a href="{% url 'add_to_cart' product.id %}">Add to Cart</a>
    </div>
{% endfor %}
{% endblock %}
```

`shop/templates/shop/cart.html`

```html
{% extends 'shop/base.html' %}

{% block content %}
<h2>Your Cart</h2>
{% for item in items %}
    <p>{{ item.product.name }} - Quantity: {{ item.quantity }}</p>
{% endfor %}
{% endblock %}
```

---

### ✅ Run the Server

```bash
python manage.py runserver
```

Visit:

* `http://127.0.0.1:8000/` → Product list
* `http://127.0.0.1:8000/cart/` → View cart

---

### 🧠 What You Learned

* How to use models with ForeignKeys (`CartItem → Product`, `CartItem → Cart`)
* How to build a cart system
* How to use `Template Inheritance`
* How to upload and serve media files (images)

---

Let me know when you're ready to add:

* Cart quantity update/remove
* Checkout functionality
* User-specific carts and login

I’ll guide you step by step.


in django admin panel why it came object ?
Excellent question! You're noticing that in the **Django admin panel**, sometimes you see labels like:

```
Cart object (1)
CartItem object (3)
```

And you're wondering — **why does it say “object” instead of something readable like “John’s cart” or “3x Apple”**?

---

### ✅ Why it says “object” in Django Admin

By **default**, Django doesn’t know how to describe your model objects, so it uses a generic fallback like:

```
<ModelName> object (<id>)
```

So if your model is `Cart`, and its `id = 1`, Django shows:

```
Cart object (1)
```

Because you haven’t yet told it *how to display the object as a string*.

---

### ✅ How to Fix It: Use `__str__` Method

To customize how your object appears in the Django admin (and elsewhere), you override the `__str__` method in your model.

---

### ✏️ Example Fix

#### For `Cart`:

Add this to your model:

```python
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
```

Now, in the admin, you’ll see something like:

```
Cart #1 - 2025-07-15 18:30
```

#### For `CartItem`:

```python
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Cart #{self.cart.id})"
```

Now the admin will show:

```
2 x Apple iPhone (Cart #1)
```

---

### ✅ Final Summary

| Problem                       | Fix                                |
| ----------------------------- | ---------------------------------- |
| Admin shows `Cart object (1)` | Django uses default string         |
| You want a friendly label     | Add `__str__` method to your model |

Let me know if you'd like help improving how the admin displays or organizes these further!



# 13 | News Aggregator         | Scrape and show news                  | BeautifulSoup, Celery, cron jobs
Hi, i am learning django with project based , so currently I want to learn | 13 | News Aggregator         | Scrape and show news                  | BeautifulSoup, Celery, cron jobs                     | as I am beginnner please give me  full code and steps regarding above and guide me with the steps please with start app 
Great! Let’s build a **Django News Aggregator App** using:

* **BeautifulSoup** (for scraping news headlines)
* **Celery** (for background scraping tasks)
* **Cron Jobs / Celery Beat** (for scheduling tasks)

---

## ✅ Step-by-Step Guide

### 🎯 Goal

Scrape latest headlines from a news site (e.g. BBC), store them in the database, and display them in your Django app.

---

### 🔧 Step 1: Setup Django Project & App

```bash
django-admin startproject newsproject
cd newsproject
python manage.py startapp newsapp
```

Add `newsapp` to `INSTALLED_APPS` in `settings.py`.

---

### 🔧 Step 2: Install Required Libraries

```bash
pip install requests beautifulsoup4
pip install celery django-celery-beat
```

---

### 📁 Step 3: Configure Celery

#### `newsproject/__init__.py`

```python
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
__all__ = ('celery_app',)
```

#### `newsproject/celery.py`

```python
from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsproject.settings')
app = Celery('newsproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

#### `settings.py`

```python
INSTALLED_APPS += ['django_celery_beat']

CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Or use RabbitMQ
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
```

---

### 🧱 Step 4: Define News Model

#### `newsapp/models.py`

```python
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🧪 Step 5: Scraping Function

#### `newsapp/tasks.py`

```python
import requests
from bs4 import BeautifulSoup
from .models import News
from celery import shared_task

@shared_task
def scrape_bbc_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.select('a.gs-c-promo-heading')[:5]

    for h in headlines:
        title = h.text.strip()
        link = 'https://www.bbc.com' + h.get('href')
        News.objects.get_or_create(title=title, link=link)
```

---

### 📆 Step 6: Schedule Scraping

```bash
python manage.py migrate django_celery_beat
```

#### `admin.py`

```python
from django.contrib import admin
from .models import News
admin.site.register(News)
```

```bash
python manage.py createsuperuser
```

Now go to Django admin → Periodic Tasks → Add new → Choose `scrape_bbc_news` → Run every 1 hour.

---

### 🎨 Step 7: Display News

#### `newsapp/views.py`

```python
from django.shortcuts import render
from .models import News

def home(request):
    news = News.objects.order_by('-published_at')
    return render(request, 'newsapp/home.html', {'news': news})
```

#### `newsapp/urls.py`

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

#### Include in `newsproject/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsapp.urls')),
]
```

---

### 📄 Step 8: HTML Template

#### `templates/newsapp/home.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>News Aggregator</title>
</head>
<body>
    <h1>Latest News</h1>
    <ul>
        {% for article in news %}
            <li><a href="{{ article.link }}">{{ article.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

Make sure your template folder is configured correctly in `settings.py`.

---

### 🚀 Step 9: Run Everything

1. Start Redis (or RabbitMQ)
2. Run Celery Worker:

   ```bash
   celery -A newsproject worker --beat --scheduler django --loglevel=info
   ```
3. Run Django:

   ```bash
   python manage.py runserver
   ```

---

Let me know if you want to use another news source or also want to add categories or search features.




Okay i run all above but my news table is empty why ? even i run all abov3 ?

Great — you're almost there! If your `News` table is still empty even after setting everything up, let’s debug step-by-step 🔍:

---

## ✅ Checkpoints to Debug Empty News Table

### 1. **Did you start Redis or RabbitMQ?**

Celery needs a **message broker** to run (usually Redis or RabbitMQ).

**If Redis:**

```bash
sudo service redis-server start
```

Or (on systems with `systemctl`):

```bash
sudo systemctl start redis
```

Then run the celery worker again:

```bash
celery -A newsproject worker --beat --scheduler django --loglevel=info
```

---

### 2. **Check if Celery worker is running successfully**

You should see log output like:

```
[INFO/MainProcess] Task newsapp.tasks.scrape_bbc_news[<task_id>] succeeded
```

If you see errors or no logs — Celery is not running correctly or not connected.

---

### 3. **Manually Trigger the Scraping Task**

Run this manually to test if scraping works:

```bash
python manage.py shell
```

Then:

```python
from newsapp.tasks import scrape_bbc_news
scrape_bbc_news()
```

Now check your DB:

```bash
python manage.py shell
from newsapp.models import News
News.objects.all()
```

✅ If this shows data — your scraping logic is fine, but Celery beat (scheduler) isn't triggering it.

---

### 4. **Check the HTML Selector is Still Valid**

News sites like **BBC** change their structure often.

In your task:

```python
headlines = soup.select('a.gs-c-promo-heading')[:5]
```

✅ Open the site `https://www.bbc.com/news` in your browser, and right-click → Inspect Element on a headline.

Check if it still has `a.gs-c-promo-heading`. If not, update your selector.

You can change it to something like:

```python
headlines = soup.find_all('a', class_='gs-c-promo-heading')
```

Also print it in shell:

```python
print([h.text for h in headlines])
```

If it's an empty list, then the scraping code isn’t finding headlines → fix selector.

---

### 5. **Check Celery Beat Schedule in Admin**

Visit `/admin/django_celery_beat/periodictask/`

✅ Make sure:

* The periodic task is active (checkbox checked)
* `scrape_bbc_news` is selected in task name
* Interval or crontab is properly set

If not — your task isn’t being scheduled.

---

### 6. **Check for Duplicates Prevention**

You have:

```python
News.objects.get_or_create(title=title, link=link)
```

If the title+link already exist, nothing new will be created. For testing, you can temporarily disable it to see raw insert:

```python
News.objects.create(title=title, link=link)
```

---

## ✅ Next Step

Once you test and verify the task manually, **focus on either:**

* Making sure **Celery worker is running** and working with Redis
* Ensuring **Celery Beat is scheduling the task properly**

---

Want me to check a specific part of your code or logs? Paste them here and I’ll help line-by-line.




# 13 : Claude | News Aggregator         | Scrape and show news                  | BeautifulSoup, Celery, cron jobs
Hi, i am learning django with project based , so currently I want to learn | 13 | News Aggregator         | Scrape and show news                  | BeautifulSoup, Celery, cron jobs                     | as I am beginnner please give me  code regarding above and guide me as i have already created django admin app with name  'projects' so  with in it  steps  with start app

## Django News Aggregator - Complete Guide

## Step 1: Create the News App

First, create a new Django app for your news aggregator:

```bash
python manage.py startapp news_aggregator
```

## Step 2: Add App to Settings

In your `settings.py`, add the new app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',  # Your existing app
    'news_aggregator',  # New app
]
```

## Step 3: Install Required Packages

Install the required packages:

```bash
pip install beautifulsoup4 requests celery redis django-celery-beat
```

## Step 4: Create Models

Create `news_aggregator/models.py`:

```python
from django.db import models
from django.utils import timezone

class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True)
    url = models.URLField()
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField()
    scraped_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-published_at']
        unique_together = ['title', 'source']
    
    def __str__(self):
        return self.title
```

## Step 5: Create Web Scraper

Create `news_aggregator/scraper.py`:

```python
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from datetime import datetime
import logging
from .models import NewsArticle, NewsSource, Category

logger = logging.getLogger(__name__)

class NewsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_bbc_news(self):
        """Scrape BBC News"""
        try:
            url = "https://www.bbc.com/news"
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get or create BBC source
            source, created = NewsSource.objects.get_or_create(
                name="BBC News",
                defaults={'url': url}
            )
            
            # Find article links
            articles = soup.find_all('a', {'data-testid': 'internal-link'})
            
            for article in articles[:10]:  # Limit to 10 articles
                try:
                    article_url = article.get('href')
                    if not article_url.startswith('http'):
                        article_url = f"https://www.bbc.com{article_url}"
                    
                    title_elem = article.find('h2') or article.find('h3')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text().strip()
                    
                    # Skip if article already exists
                    if NewsArticle.objects.filter(title=title, source=source).exists():
                        continue
                    
                    # Get article content
                    article_response = self.session.get(article_url)
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')
                    
                    # Extract content
                    content_div = article_soup.find('div', {'data-component': 'text-block'})
                    content = content_div.get_text().strip() if content_div else "Content not available"
                    
                    # Extract image
                    img_tag = article_soup.find('img')
                    image_url = img_tag.get('src') if img_tag else ""
                    
                    # Create article
                    NewsArticle.objects.create(
                        title=title,
                        content=content,
                        url=article_url,
                        source=source,
                        image_url=image_url,
                        published_at=timezone.now(),
                        summary=content[:200] + "..." if len(content) > 200 else content
                    )
                    
                except Exception as e:
                    logger.error(f"Error scraping article: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error scraping BBC News: {e}")
    
    def scrape_reddit_news(self):
        """Scrape Reddit News"""
        try:
            url = "https://www.reddit.com/r/news/"
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get or create Reddit source
            source, created = NewsSource.objects.get_or_create(
                name="Reddit News",
                defaults={'url': url}
            )
            
            # Find posts
            posts = soup.find_all('h3')
            
            for post in posts[:10]:
                try:
                    link = post.find('a')
                    if not link:
                        continue
                    
                    title = link.get_text().strip()
                    post_url = link.get('href')
                    
                    if not post_url.startswith('http'):
                        post_url = f"https://www.reddit.com{post_url}"
                    
                    # Skip if article already exists
                    if NewsArticle.objects.filter(title=title, source=source).exists():
                        continue
                    
                    NewsArticle.objects.create(
                        title=title,
                        content="Reddit post - click to view full content",
                        url=post_url,
                        source=source,
                        published_at=timezone.now(),
                        summary=title
                    )
                    
                except Exception as e:
                    logger.error(f"Error scraping Reddit post: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error scraping Reddit: {e}")
    
    def scrape_all_sources(self):
        """Scrape all active sources"""
        self.scrape_bbc_news()
        self.scrape_reddit_news()
        logger.info("Scraping completed for all sources")
```

## Step 6: Create Celery Tasks

Create `news_aggregator/tasks.py`:

```python
from celery import shared_task
from .scraper import NewsScraper
import logging

logger = logging.getLogger(__name__)

@shared_task
def scrape_news():
    """Celery task to scrape news"""
    try:
        scraper = NewsScraper()
        scraper.scrape_all_sources()
        logger.info("News scraping task completed successfully")
        return "News scraping completed"
    except Exception as e:
        logger.error(f"Error in news scraping task: {e}")
        return f"Error: {e}"

@shared_task
def cleanup_old_articles():
    """Remove articles older than 30 days"""
    from django.utils import timezone
    from datetime import timedelta
    from .models import NewsArticle
    
    cutoff_date = timezone.now() - timedelta(days=30)
    deleted_count = NewsArticle.objects.filter(published_at__lt=cutoff_date).delete()[0]
    logger.info(f"Deleted {deleted_count} old articles")
    return f"Deleted {deleted_count} old articles"
```

## Step 7: Create Views

Create `news_aggregator/views.py`:

```python
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import NewsArticle, Category, NewsSource

def news_list(request):
    """Display list of news articles"""
    articles = NewsArticle.objects.filter(is_active=True)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        articles = articles.filter(category_id=category_id)
    
    # Filter by source
    source_id = request.GET.get('source')
    if source_id:
        articles = articles.filter(source_id=source_id)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articles': page_obj,
        'categories': Category.objects.all(),
        'sources': NewsSource.objects.filter(is_active=True),
        'current_category': category_id,
        'current_source': source_id,
        'query': query,
    }
    
    return render(request, 'news_aggregator/news_list.html', context)

def news_detail(request, pk):
    """Display single news article"""
    article = get_object_or_404(NewsArticle, pk=pk, is_active=True)
    
    # Get related articles
    related_articles = NewsArticle.objects.filter(
        source=article.source,
        is_active=True
    ).exclude(pk=pk)[:5]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'news_aggregator/news_detail.html', context)

def trigger_scraping(request):
    """Manually trigger news scraping"""
    from .tasks import scrape_news
    
    if request.method == 'POST':
        scrape_news.delay()
        return render(request, 'news_aggregator/scraping_triggered.html')
    
    return render(request, 'news_aggregator/trigger_scraping.html')
```

## Step 8: Create Templates

Create the templates directory: `news_aggregator/templates/news_aggregator/`

**base.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}News Aggregator{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'news_aggregator:news_list' %}">News Aggregator</a>
            <div class="navbar-nav">
                <a class="nav-link" href="{% url 'news_aggregator:news_list' %}">Home</a>
                <a class="nav-link" href="{% url 'news_aggregator:trigger_scraping' %}">Scrape News</a>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**news_list.html:**
```html
{% extends 'news_aggregator/base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-3">
        <h5>Filters</h5>
        
        <!-- Search Form -->
        <form method="get" class="mb-3">
            <input type="text" name="q" class="form-control" placeholder="Search news..." value="{{ query }}">
            <button type="submit" class="btn btn-primary btn-sm mt-2">Search</button>
        </form>
        
        <!-- Categories -->
        <div class="mb-3">
            <h6>Categories</h6>
            <ul class="list-unstyled">
                <li><a href="{% url 'news_aggregator:news_list' %}">All Categories</a></li>
                {% for category in categories %}
                <li>
                    <a href="?category={{ category.id }}">{{ category.name }}</a>
                </li>
                {% endfor %}
            </ul>
        </div>
        
        <!-- Sources -->
        <div class="mb-3">
            <h6>Sources</h6>
            <ul class="list-unstyled">
                <li><a href="{% url 'news_aggregator:news_list' %}">All Sources</a></li>
                {% for source in sources %}
                <li>
                    <a href="?source={{ source.id }}">{{ source.name }}</a>
                </li>
                {% endfor %}
            </ul>
        </div>
    </div>
    
    <div class="col-md-9">
        <h2>Latest News</h2>
        
        {% for article in articles %}
        <div class="card mb-3">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="{% url 'news_aggregator:news_detail' article.pk %}">{{ article.title }}</a>
                </h5>
                <p class="card-text">{{ article.summary }}</p>
                <p class="card-text">
                    <small class="text-muted">
                        {{ article.source.name }} • {{ article.published_at|date:"M d, Y H:i" }}
                    </small>
                </p>
            </div>
        </div>
        {% empty %}
        <p>No news articles found.</p>
        {% endfor %}
        
        <!-- Pagination -->
        {% if articles.has_other_pages %}
        <nav aria-label="Page navigation">
            <ul class="pagination">
                {% if articles.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ articles.previous_page_number }}">Previous</a>
                </li>
                {% endif %}
                
                {% for num in articles.paginator.page_range %}
                {% if articles.number == num %}
                <li class="page-item active">
                    <span class="page-link">{{ num }}</span>
                </li>
                {% else %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                </li>
                {% endif %}
                {% endfor %}
                
                {% if articles.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ articles.next_page_number }}">Next</a>
                </li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
    </div>
</div>
{% endblock %}
```

**news_detail.html:**
```html
{% extends 'news_aggregator/base.html' %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <article>
            <h1>{{ article.title }}</h1>
            
            <div class="mb-3">
                <small class="text-muted">
                    {{ article.source.name }} • {{ article.published_at|date:"M d, Y H:i" }}
                </small>
            </div>
            
            {% if article.image_url %}
            <img src="{{ article.image_url }}" class="img-fluid mb-3" alt="{{ article.title }}">
            {% endif %}
            
            <div class="article-content">
                {{ article.content|linebreaks }}
            </div>
            
            <div class="mt-3">
                <a href="{{ article.url }}" target="_blank" class="btn btn-primary">Read Original Article</a>
            </div>
        </article>
    </div>
    
    <div class="col-md-4">
        <h5>Related Articles</h5>
        {% for related in related_articles %}
        <div class="card mb-2">
            <div class="card-body">
                <h6 class="card-title">
                    <a href="{% url 'news_aggregator:news_detail' related.pk %}">{{ related.title }}</a>
                </h6>
                <small class="text-muted">{{ related.published_at|date:"M d, Y" }}</small>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

## Step 9: Create URLs

Create `news_aggregator/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'news_aggregator'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('article/<int:pk>/', views.news_detail, name='news_detail'),
    path('scrape/', views.trigger_scraping, name='trigger_scraping'),
]
```

Update your main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_aggregator.urls')),
]
```

## Step 10: Configure Admin

Create `news_aggregator/admin.py`:

```python
from django.contrib import admin
from .models import NewsSource, Category, NewsArticle

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'category', 'published_at', 'is_active']
    list_filter = ['source', 'category', 'is_active', 'published_at']
    search_fields = ['title', 'content']
    readonly_fields = ['scraped_at']
```

## Step 11: Configure Celery

Create `celery.py` in your project root:

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projects.settings')

app = Celery('projects')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

Add to your `settings.py`:

```python
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat Configuration
CELERY_BEAT_SCHEDULE = {
    'scrape-news-every-hour': {
        'task': 'news_aggregator.tasks.scrape_news',
        'schedule': 3600.0,  # Every hour
    },
    'cleanup-old-articles-daily': {
        'task': 'news_aggregator.tasks.cleanup_old_articles',
        'schedule': 86400.0,  # Every day
    },
}
```

## Step 12: Run the Application

1. Make and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser:
```bash
python manage.py createsuperuser
```

3. Start Redis server:
```bash
redis-server
```

4. Start Celery worker (in another terminal):
```bash
celery -A projects worker --loglevel=info
```

5. Start Celery beat (in another terminal):
```bash
celery -A projects beat --loglevel=info
```

6. Run Django development server:
```bash
python manage.py runserver
```

## Next Steps

1. **Add more news sources**: Extend the scraper to include more websites
2. **Implement caching**: Use Redis for caching frequently accessed data
3. **Add RSS feed support**: Parse RSS feeds for easier news aggregation
4. **Implement user authentication**: Allow users to save favorite articles
5. **Add email notifications**: Send daily news summaries to users
6. **Improve error handling**: Add more robust error handling and logging
7. **Add tests**: Write unit and integration tests for your application

This complete news aggregator will scrape news from multiple sources, display them in a clean interface, and automatically update using Celery tasks!


# 14  | Chat App                | Simple room-based chat                | WebSockets, Django Channels 
Hi, i am learning django with project based , so currently I want to learn | 14 | Chat App                | Simple room-based chat                | WebSockets, Django Channels                          | as I am beginnner please give me  code regarding above and guide me as i have already created django admin app with name  'projects' so  with in it  steps  with start app


##  Django Chat App with WebSockets - Complete Guide

## Step 1: Create the Chat App

First, create a new Django app for your chat application:

```bash
python manage.py startapp chat
```

## Step 2: Install Required Packages

Install Django Channels and other required packages:

```bash
pip install channels channels-redis
```

## Step 3: Configure Settings

Update your `settings.py`:

```python
# settings.py

import os
from pathlib import Path

# ... your existing settings ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',  # Add this
    'chat',      # Add your chat app
]

# ... your existing settings ...

# Channels Configuration
ASGI_APPLICATION = 'projects.asgi.application'

# Channel layer configuration (using Redis)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# For development, you can use in-memory channel layer (not recommended for production)
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer'
#     }
# }
```

## Step 4: Configure ASGI

Create `asgi.py` in your project root (same level as `settings.py`):

```python
# projects/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projects.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})
```

## Step 5: Create Models

Create `chat/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/chat/room/{self.name}/'

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'

class RoomMember(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['room', 'user']
    
    def __str__(self):
        return f'{self.user.username} in {self.room.name}'
```

## Step 6: Create WebSocket Consumer

Create `chat/consumers.py`:

```python
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message, RoomMember

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Update user online status
        await self.update_user_online_status(True)
        
        # Send user joined message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'user': self.user.username,
                'message': f'{self.user.username} joined the chat'
            }
        )

    async def disconnect(self, close_code):
        # Update user online status
        await self.update_user_online_status(False)
        
        # Send user left message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_left',
                'user': self.user.username,
                'message': f'{self.user.username} left the chat'
            }
        )
        
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Save message to database
        await self.save_message(message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'timestamp': self.get_timestamp()
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
            'timestamp': timestamp
        }))

    async def user_joined(self, event):
        user = event['user']
        message = event['message']
        
        # Send user joined message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_joined',
            'user': user,
            'message': message
        }))

    async def user_left(self, event):
        user = event['user']
        message = event['message']
        
        # Send user left message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_left',
            'user': user,
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, message):
        room = Room.objects.get(name=self.room_name)
        Message.objects.create(
            room=room,
            user=self.user,
            content=message
        )

    @database_sync_to_async
    def update_user_online_status(self, is_online):
        room = Room.objects.get(name=self.room_name)
        room_member, created = RoomMember.objects.get_or_create(
            room=room,
            user=self.user,
            defaults={'is_online': is_online}
        )
        if not created:
            room_member.is_online = is_online
            room_member.save()

    def get_timestamp(self):
        from django.utils import timezone
        return timezone.now().strftime('%Y-%m-%d %H:%M:%S')
```

## Step 7: Create WebSocket Routing

Create `chat/routing.py`:

```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```

## Step 8: Create Views

Create `chat/views.py`:

```python
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
```

## Step 9: Create Forms

Create `chat/forms.py`:

```python
from django import forms
from .models import Room

class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'is_private']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter room description (optional)'
            }),
            'is_private': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        # Remove spaces and convert to lowercase
        name = name.replace(' ', '_').lower()
        return name
```

## Step 10: Create Templates

Create the templates directory: `chat/templates/chat/`

**base.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Chat App{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .chat-container {
            height: 500px;
            overflow-y: auto;
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 0.375rem;
        }
        .message {
            margin-bottom: 10px;
            padding: 8px 12px;
            border-radius: 18px;
            max-width: 70%;
            word-wrap: break-word;
        }
        .message.own {
            background-color: #007bff;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .message.other {
            background-color: #e9ecef;
            color: #495057;
        }
        .system-message {
            text-align: center;
            color: #6c757d;
            font-style: italic;
            margin: 10px 0;
        }
        .online-indicator {
            color: #28a745;
        }
        .offline-indicator {
            color: #6c757d;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'chat:home' %}">
                <i class="fas fa-comments"></i> Chat App
            </a>
            <div class="navbar-nav ms-auto">
                {% if user.is_authenticated %}
                    <a class="nav-link" href="{% url 'chat:room_list' %}">Rooms</a>
                    <a class="nav-link" href="{% url 'chat:create_room' %}">Create Room</a>
                    <span class="navbar-text">Hello, {{ user.username }}!</span>
                    <a class="nav-link" href="{% url 'admin:logout' %}">Logout</a>
                {% else %}
                    <a class="nav-link" href="{% url 'chat:register' %}">Register</a>
                    <a class="nav-link" href="{% url 'admin:login' %}">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block javascript %}{% endblock %}
</body>
</html>
```

**home.html:**
```html
{% extends 'chat/base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="text-center mb-4">
            <h1><i class="fas fa-comments"></i> Welcome to Chat App</h1>
            <p class="lead">Connect with others in real-time chat rooms</p>
        </div>

        {% if user.is_authenticated %}
            <div class="row mb-4">
                <div class="col-md-6">
                    <a href="{% url 'chat:room_list' %}" class="btn btn-primary btn-lg w-100">
                        <i class="fas fa-list"></i> Browse Rooms
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="{% url 'chat:create_room' %}" class="btn btn-success btn-lg w-100">
                        <i class="fas fa-plus"></i> Create Room
                    </a>
                </div>
            </div>

            <h3>Recent Rooms</h3>
            <div class="row">
                {% for room in rooms %}
                <div class="col-md-6 mb-3">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">{{ room.name }}</h5>
                            <p class="card-text">{{ room.description|truncatewords:10 }}</p>
                            <small class="text-muted">Created by {{ room.created_by.username }}</small>
                            <div class="mt-2">
                                <a href="{% url 'chat:room_detail' room.name %}" class="btn btn-primary">
                                    Join Chat
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                {% empty %}
                <p>No chat rooms available. <a href="{% url 'chat:create_room' %}">Create one!</a></p>
                {% endfor %}
            </div>
        {% else %}
            <div class="text-center">
                <p>Please login or register to start chatting</p>
                <a href="{% url 'admin:login' %}" class="btn btn-primary me-2">Login</a>
                <a href="{% url 'chat:register' %}" class="btn btn-secondary">Register</a>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

**room_detail.html:**
```html
{% extends 'chat/base.html' %}

{% block title %}{{ room.name }} - Chat{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-9">
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-comments"></i> {{ room.name }}</h4>
                <small class="text-muted">{{ room.description }}</small>
            </div>
            <div class="card-body">
                <div id="chat-messages" class="chat-container p-3 mb-3"></div>
                <div class="input-group">
                    <input type="text" id="chat-message-input" class="form-control" placeholder="Type a message..." maxlength="500">
                    <button class="btn btn-primary" id="chat-message-submit">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-3">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-users"></i> Online Users</h5>
            </div>
            <div class="card-body">
                <div id="online-users">
                    {% for member in online_members %}
                    <div class="mb-2">
                        <i class="fas fa-circle online-indicator"></i>
                        {{ member.user.username }}
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>

{{ room_name_json|json_script:"room-name" }}
<script>
    const roomName = JSON.parse(document.getElementById('room-name').textContent);
    const currentUser = '{{ user.username }}';
    
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );
    
    const chatMessages = document.querySelector('#chat-messages');
    const messageInput = document.querySelector('#chat-message-input');
    const messageSubmit = document.querySelector('#chat-message-submit');
    
    // Load existing messages
    {% for message in messages %}
    addMessage('{{ message.user.username }}', '{{ message.content|escapejs }}', '{{ message.timestamp|date:"H:i" }}');
    {% endfor %}
    
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        
        if (data.type === 'chat_message') {
            addMessage(data.user, data.message, data.timestamp);
        } else if (data.type === 'user_joined') {
            addSystemMessage(data.message);
        } else if (data.type === 'user_left') {
            addSystemMessage(data.message);
        }
    };
    
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
    
    function addMessage(user, message, timestamp) {
        const messageElement = document.createElement('div');
        const isOwnMessage = user === currentUser;
        
        messageElement.classList.add('message');
        messageElement.classList.add(isOwnMessage ? 'own' : 'other');
        
        messageElement.innerHTML = `
            <div><strong>${user}</strong> <small>${timestamp}</small></div>
            <div>${message}</div>
        `;
        
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function addSystemMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('system-message');
        messageElement.textContent = message;
        
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function sendMessage() {
        const message = messageInput.value.trim();
        if (message) {
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInput.value = '';
        }
    }
    
    messageSubmit.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Auto-scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
</script>
{% endblock %}
```

**create_room.html:**
```html
{% extends 'chat/base.html' %}

{% block title %}Create Room{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-6 mx-auto">
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-plus"></i> Create New Room</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.name.id_for_label }}" class="form-label">Room Name</label>
                        {{ form.name }}
                        {% if form.name.errors %}
                            <div class="text-danger">{{ form.name.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">Description</label>
                        {{ form.description }}
                        {% if form.description.errors %}
                            <div class="text-danger">{{ form.description.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3 form-check">
                        {{ form.is_private }}
                        <label class="form-check-label" for="{{ form.is_private.id_for_label }}">
                            Private Room
                        </label>
                    </div>
                    
                    <button type="submit" class="btn btn-success">
                        <i class="fas fa-plus"></i> Create Room
                    </button>
                    <a href="{% url 'chat:home' %}" class="btn btn-secondary">Cancel</a>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## Step 11: Create URLs

Create `chat/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('room/<str:room_name>/', views.room_detail, name='room_detail'),
    path('create-room/', views.create_room, name='create_room'),
    path('register/', views.register, name='register'),
    path('api/room/<str:room_name>/messages/', views.get_room_messages, name='get_room_messages'),
]
```

Update your main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', include('chat.urls')),  # Make chat the default app
]
```

## Step 12: Configure Admin

Create `chat/admin.py`:

```python
from django.contrib import admin
from .models import Room, Message, RoomMember

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at', 'is_private']
    list_filter = ['is_private', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'content', 'timestamp']
    list_filter = ['room', 'timestamp']
    search_fields = ['content', 'user__username']
    readonly_fields = ['timestamp']

@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'joined_at', 'is_online']
    list_filter = ['is_online', 'joined_at']
    search_fields = ['user__username', 'room__name']
```

## Step 13: Run the Application

1. **Install Redis** (required for Django Channels):
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install redis-server
   
   # On macOS
   brew install redis
   
   # On Windows, download from https://github.com/microsoftarchive/redis/releases
   ```

2. **Make and apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Redis server**:
   ```bash
   redis-server
   ```

5. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

## Step 14: Testing the Chat App

1. Visit `http://127.0.0.1:8000/`
2. Register a new user or login with superuser
3. Create a new chat room
4. Open multiple browser tabs/windows to test real-time messaging
5. Try joining the same room from different browsers to see real-time chat

## Features Implemented

✅ **Real-time messaging** with WebSockets
✅ **Room-based chat** system
✅ **User authentication** and registration
✅ **Online/offline status** tracking
✅ **Message history** storage
✅ **Responsive design** with Bootstrap
✅ **Admin interface** for management
✅ **System messages** for user join/leave events

## Next Steps for Enhancement

1. **File sharing**: Allow users to share images/files
2. **Private messaging**: Direct messages between users
3. **Message reactions**: Like/react to messages
4. **Message editing/deletion**: Edit or delete sent messages
5. **Voice/video calls**: WebRTC integration
6. **Push notifications**: Real-time notifications
7. **Message search**: Search through chat history
8. **User profiles**: Extended user information
9. **Room moderation**: Admin controls for rooms
10. **Message encryption**: End-to-end encryption

This chat application provides a solid foundation for real-time communication and demonstrates key concepts like WebSockets, Django Channels, and asynchronous programming!



# 15 | Job Board               | Post and apply for jobs               | Advanced models, relations, email                    |
# Django Job Board - Complete Guide

## Step 1: Create the App

First, navigate to your project directory and create the job board app:

```bash
cd projects
python manage.py startapp jobboard
```

## Step 2: Add App to Settings

In `projects/settings.py`, add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobboard',  # Add this line
]
```

## Step 3: Create Models

Create `jobboard/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Companies"
    
    def __str__(self):
        return self.name

class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Job Categories"
    
    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    ]
    
    EXPERIENCE_LEVELS = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('lead', 'Lead/Manager'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    requirements = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='full_time')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS, default='entry')
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    application_deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})
    
    def is_deadline_passed(self):
        return timezone.now() > self.application_deadline

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interviewed', 'Interviewed'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['job', 'applicant']  # Prevent duplicate applications
        ordering = ['-applied_at']
    
    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    skills = models.TextField(blank=True, help_text="Comma-separated skills")
    experience_years = models.IntegerField(default=0)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
```

## Step 4: Create Forms

Create `jobboard/forms.py`:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job, JobApplication, Company, UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'category', 'description', 'requirements', 
                 'salary_min', 'salary_max', 'job_type', 'experience_level', 
                 'location', 'application_deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'requirements': forms.Textarea(attrs={'rows': 5}),
            'application_deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter', 'resume']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Write your cover letter here...'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'phone', 'location', 'skills', 'experience_years', 'linkedin_url', 'github_url']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Python, Django, JavaScript, etc.'}),
        }
```

## Step 5: Create Views

Create `jobboard/views.py`:

```python
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
```

## Step 6: Create URLs

Create `jobboard/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('job/<int:pk>/applications/', views.job_applications, name='job_applications'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
```

Update `projects/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Step 7: Create Templates

Create the following directory structure:
```
jobboard/
├── templates/
│   ├── jobboard/
│   │   ├── base.html
│   │   ├── job_list.html
│   │   ├── job_detail.html
│   │   ├── apply_job.html
│   │   ├── post_job.html
│   │   ├── my_jobs.html
│   │   ├── my_applications.html
│   │   ├── job_applications.html
│   │   └── profile.html
│   └── registration/
│       ├── login.html
│       └── register.html
```

## Step 8: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 9: Create Admin Configuration

Update `jobboard/admin.py`:

```python
from django.contrib import admin
from .models import Job, JobApplication, Company, UserProfile, JobCategory

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']
    search_fields = ['name']

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'is_active', 'created_at']
    list_filter = ['job_type', 'is_active', 'created_at']
    search_fields = ['title', 'company__name']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['applicant__username', 'job__title']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'experience_years']
    search_fields = ['user__username', 'location']
```

## Step 10: Update Settings for Email and Media

Add to `projects/settings.py`:

```python
import os

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email settings (for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'your_email@example.com'

# For production, use:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your_app_password'
```

## Next Steps

1. Create the HTML templates (I can provide these if needed)
2. Add CSS styling for better UI
3. Test the application
4. Add more features like:
   - Job bookmarking
   - Advanced search filters
   - Email notifications
   - Job recommendations

This job board includes:
- User registration and authentication
- Job posting and management
- Job applications with file uploads
- Email notifications
- User profiles
- Search and filtering
- Admin interface

Would you like me to provide the HTML templates or help with any specific part?



<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Job Board{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'job_list' %}">
                <i class="fas fa-briefcase"></i> Job Board
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'job_list' %}">Jobs</a>
                    </li>
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'post_job' %}">Post Job</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'my_jobs' %}">My Jobs</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'my_applications' %}">My Applications</a>
                        </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
                                <i class="fas fa-user"></i> {{ user.username }}
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="{% url 'profile' %}">Profile</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
                            </ul>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'register' %}">Register</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <main class="container mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

<!-- job_list.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Job Listings - Job Board{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-3">
        <div class="card">
            <div class="card-header">
                <h5>Filter Jobs</h5>
            </div>
            <div class="card-body">
                <form method="get">
                    <div class="mb-3">
                        <label for="search" class="form-label">Search</label>
                        <input type="text" class="form-control" id="search" name="search" value="{{ search_query }}" placeholder="Job title, company, location...">
                    </div>
                    
                    <div class="mb-3">
                        <label for="category" class="form-label">Category</label>
                        <select class="form-select" id="category" name="category">
                            <option value="">All Categories</option>
                            {% for category in categories %}
                                <option value="{{ category.id }}" {% if category.id|stringformat:"s" == selected_category %}selected{% endif %}>
                                    {{ category.name }}
                                </option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <div class="mb-3">
                        <label for="job_type" class="form-label">Job Type</label>
                        <select class="form-select" id="job_type" name="job_type">
                            <option value="">All Types</option>
                            <option value="full_time" {% if selected_job_type == 'full_time' %}selected{% endif %}>Full Time</option>
                            <option value="part_time" {% if selected_job_type == 'part_time' %}selected{% endif %}>Part Time</option>
                            <option value="contract" {% if selected_job_type == 'contract' %}selected{% endif %}>Contract</option>
                            <option value="internship" {% if selected_job_type == 'internship' %}selected{% endif %}>Internship</option>
                            <option value="remote" {% if selected_job_type == 'remote' %}selected{% endif %}>Remote</option>
                        </select>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">Filter</button>
                    <a href="{% url 'job_list' %}" class="btn btn-secondary">Clear</a>
                </form>
            </div>
        </div>
    </div>
    
    <div class="col-md-9">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h2>Job Listings</h2>
            {% if user.is_authenticated %}
                <a href="{% url 'post_job' %}" class="btn btn-success">
                    <i class="fas fa-plus"></i> Post Job
                </a>
            {% endif %}
        </div>
        
        {% if page_obj %}
            {% for job in page_obj %}
                <div class="card mb-3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-8">
                                <h5 class="card-title">
                                    <a href="{% url 'job_detail' job.pk %}" class="text-decoration-none">
                                        {{ job.title }}
                                    </a>
                                </h5>
                                <p class="text-muted mb-1">
                                    <i class="fas fa-building"></i> {{ job.company.name }}
                                </p>
                                <p class="text-muted mb-1">
                                    <i class="fas fa-map-marker-alt"></i> {{ job.location }}
                                </p>
                                <p class="card-text">{{ job.description|truncatewords:20 }}</p>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-secondary">{{ job.get_job_type_display }}</span>
                                    <span class="badge bg-info">{{ job.get_experience_level_display }}</span>
                                    {% if job.category %}
                                        <span class="badge bg-primary">{{ job.category.name }}</span>
                                    {% endif %}
                                </div>
                            </div>
                            <div class="col-md-4 text-end">
                                {% if job.salary_min and job.salary_max %}
                                    <p class="text-success fw-bold mb-2">
                                        ${{ job.salary_min|floatformat:0 }} - ${{ job.salary_max|floatformat:0 }}
                                    </p>
                                {% endif %}
                                <p class="text-muted small">{{ job.created_at|date:"M d, Y" }}</p>
                                <a href="{% url 'job_detail' job.pk %}" class="btn btn-primary">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
            
            <!-- Pagination -->
            {% if page_obj.has_other_pages %}
                <nav aria-label="Page navigation">
                    <ul class="pagination justify-content-center">
                        {% if page_obj.has_previous %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}{% if selected_category %}&category={{ selected_category }}{% endif %}{% if selected_job_type %}&job_type={{ selected_job_type }}{% endif %}">Previous</a>
                            </li>
                        {% endif %}
                        
                        {% for num in page_obj.paginator.page_range %}
                            {% if page_obj.number == num %}
                                <li class="page-item active">
                                    <span class="page-link">{{ num }}</span>
                                </li>
                            {% else %}
                                <li class="page-item">
                                    <a class="page-link" href="?page={{ num }}{% if search_query %}&search={{ search_query }}{% endif %}{% if selected_category %}&category={{ selected_category }}{% endif %}{% if selected_job_type %}&job_type={{ selected_job_type }}{% endif %}">{{ num }}</a>
                                </li>
                            {% endif %}
                        {% endfor %}
                        
                        {% if page_obj.has_next %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}{% if selected_category %}&category={{ selected_category }}{% endif %}{% if selected_job_type %}&job_type={{ selected_job_type }}{% endif %}">Next</a>
                            </li>
                        {% endif %}
                    </ul>
                </nav>
            {% endif %}
        {% else %}
            <div class="alert alert-info">
                <i class="fas fa-info-circle"></i> No jobs found matching your criteria.
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}

<!-- job_detail.html -->
{% extends 'jobboard/base.html' %}

{% block title %}{{ job.title }} - Job Board{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-start mb-3">
                    <div>
                        <h1 class="card-title">{{ job.title }}</h1>
                        <h5 class="text-muted">
                            <i class="fas fa-building"></i> {{ job.company.name }}
                        </h5>
                    </div>
                    {% if job.company.logo %}
                        <img src="{{ job.company.logo.url }}" alt="{{ job.company.name }}" class="img-thumbnail" style="max-width: 100px;">
                    {% endif %}
                </div>
                
                <div class="row mb-3">
                    <div class="col-md-6">
                        <p><i class="fas fa-map-marker-alt"></i> <strong>Location:</strong> {{ job.location }}</p>
                        <p><i class="fas fa-clock"></i> <strong>Type:</strong> {{ job.get_job_type_display }}</p>
                        <p><i class="fas fa-chart-line"></i> <strong>Experience:</strong> {{ job.get_experience_level_display }}</p>
                    </div>
                    <div class="col-md-6">
                        {% if job.salary_min and job.salary_max %}
                            <p><i class="fas fa-dollar-sign"></i> <strong>Salary:</strong> ${{ job.salary_min|floatformat:0 }} - ${{ job.salary_max|floatformat:0 }}</p>
                        {% endif %}
                        {% if job.category %}
                            <p><i class="fas fa-tag"></i> <strong>Category:</strong> {{ job.category.name }}</p>
                        {% endif %}
                        <p><i class="fas fa-calendar"></i> <strong>Deadline:</strong> {{ job.application_deadline|date:"M d, Y H:i" }}</p>
                    </div>
                </div>
                
                <hr>
                
                <div class="mb-4">
                    <h4>Job Description</h4>
                    <div class="job-content">{{ job.description|linebreaks }}</div>
                </div>
                
                <div class="mb-4">
                    <h4>Requirements</h4>
                    <div class="job-content">{{ job.requirements|linebreaks }}</div>
                </div>
                
                {% if job.company.description %}
                    <div class="mb-4">
                        <h4>About {{ job.company.name }}</h4>
                        <p>{{ job.company.description }}</p>
                        {% if job.company.website %}
                            <a href="{{ job.company.website }}" target="_blank" class="btn btn-outline-primary btn-sm">
                                <i class="fas fa-external-link-alt"></i> Visit Website
                            </a>
                        {% endif %}
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>Apply for this Job</h5>
            </div>
            <div class="card-body">
                {% if user.is_authenticated %}
                    {% if user_has_applied %}
                        <div class="alert alert-info">
                            <i class="fas fa-check-circle"></i> You have already applied for this job.
                        </div>
                        <a href="{% url 'my_applications' %}" class="btn btn-outline-primary">View My Applications</a>
                    {% elif job.is_deadline_passed %}
                        <div class="alert alert-warning">
                            <i class="fas fa-exclamation-triangle"></i> Application deadline has passed.
                        </div>
                    {% else %}
                        <a href="{% url 'apply_job' job.pk %}" class="btn btn-success btn-lg w-100">
                            <i class="fas fa-paper-plane"></i> Apply Now
                        </a>
                    {% endif %}
                {% else %}
                    <p>Please <a href="{% url 'login' %}">login</a> to apply for this job.</p>
                    <a href="{% url 'login' %}" class="btn btn-primary">Login</a>
                    <a href="{% url 'register' %}" class="btn btn-outline-primary">Register</a>
                {% endif %}
            </div>
        </div>
        
        <div class="card mt-3">
            <div class="card-header">
                <h5>Job Details</h5>
            </div>
            <div class="card-body">
                <p><strong>Posted:</strong> {{ job.created_at|date:"M d, Y" }}</p>
                <p><strong>Applications:</strong> {{ job.applications.count }}</p>
                <p><strong>Job ID:</strong> #{{ job.id }}</p>
                
                {% if user == job.created_by %}
                    <hr>
                    <div class="d-grid gap-2">
                        <a href="{% url 'job_applications' job.pk %}" class="btn btn-primary">
                            <i class="fas fa-users"></i> View Applications ({{ job.applications.count }})
                        </a>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- apply_job.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Apply for {{ job.title }} - Job Board{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h4>Apply for {{ job.title }}</h4>
                <p class="text-muted mb-0">at {{ job.company.name }}</p>
            </div>
            <div class="card-body">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.cover_letter.id_for_label }}" class="form-label">Cover Letter *</label>
                        {{ form.cover_letter }}
                        {% if form.cover_letter.errors %}
                            <div class="text-danger">{{ form.cover_letter.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.resume.id_for_label }}" class="form-label">Resume *</label>
                        {{ form.resume }}
                        {% if form.resume.errors %}
                            <div class="text-danger">{{ form.resume.errors }}</div>
                        {% endif %}
                        <div class="form-text">Upload your resume (PDF, DOC, DOCX files only)</div>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'job_detail' job.pk %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-success">
                            <i class="fas fa-paper-plane"></i> Submit Application
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- post_job.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Post a Job - Job Board{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h4>Post a New Job</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.title.id_for_label }}" class="form-label">Job Title *</label>
                                {{ form.title }}
                                {% if form.title.errors %}
                                    <div class="text-danger">{{ form.title.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.company.id_for_label }}" class="form-label">Company *</label>
                                {{ form.company }}
                                {% if form.company.errors %}
                                    <div class="text-danger">{{ form.company.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.category.id_for_label }}" class="form-label">Category</label>
                                {{ form.category }}
                                {% if form.category.errors %}
                                    <div class="text-danger">{{ form.category.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.location.id_for_label }}" class="form-label">Location *</label>
                                {{ form.location }}
                                {% if form.location.errors %}
                                    <div class="text-danger">{{ form.location.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">Job Description *</label>
                        {{ form.description }}
                        {% if form.description.errors %}
                            <div class="text-danger">{{ form.description.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.requirements.id_for_label }}" class="form-label">Requirements *</label>
                        {{ form.requirements }}
                        {% if form.requirements.errors %}
                            <div class="text-danger">{{ form.requirements.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.salary_min.id_for_label }}" class="form-label">Minimum Salary</label>
                                {{ form.salary_min }}
                                {% if form.salary_min.errors %}
                                    <div class="text-danger">{{ form.salary_min.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.salary_max.id_for_label }}" class="form-label">Maximum Salary</label>
                                {{ form.salary_max }}
                                {% if form.salary_max.errors %}
                                    <div class="text-danger">{{ form.salary_max.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.job_type.id_for_label }}" class="form-label">Job Type *</label>
                                {{ form.job_type }}
                                {% if form.job_type.errors %}
                                    <div class="text-danger">{{ form.job_type.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.experience_level.id_for_label }}" class="form-label">Experience Level *</label>
                                {{ form.experience_level }}
                                {% if form.experience_level.errors %}
                                    <div class="text-danger">{{ form.experience_level.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.application_deadline.id_for_label }}" class="form-label">Application Deadline *</label>
                        {{ form.application_deadline }}
                        {% if form.application_deadline.errors %}
                            <div class="text-danger">{{ form.application_deadline.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'job_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-success">
                            <i class="fas fa-plus"></i> Post Job
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- login.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Login - Job Board{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4>Login</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">Username</label>
                        {{ form.username }}
                        {% if form.username.errors %}
                            <div class="text-danger">{{ form.username.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password.id_for_label }}" class="form-label">Password</label>
                        {{ form.password }}
                        {% if form.password.errors %}
                            <div class="text-danger">{{ form.password.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Login</button>
                    </div>
                </form>
                
                <div class="text-center mt-3">
                    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- register.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Register - Job Board{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4>Register</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">Username</label>
                        {{ form.username }}
                        {% if form.username.errors %}
                            <div class="text-danger">{{ form.username.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.first_name.id_for_label }}" class="form-label">First Name</label>
                                {{ form.first_name }}
                                {% if form.first_name.errors %}
                                    <div class="text-danger">{{ form.first_name.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="{{ form.last_name.id_for_label }}" class="form-label">Last Name</label>
                                {{ form.last_name }}
                                {% if form.last_name.errors %}
                                    <div class="text-danger">{{ form.last_name.errors }}</div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.email.id_for_label }}" class="form-label">Email</label>
                        {{ form.email }}
                        {% if form.email.errors %}
                            <div class="text-danger">{{ form.email.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password1.id_for_label }}" class="form-label">Password</label>
                        {{ form.password1 }}
                        {% if form.password1.errors %}
                            <div class="text-danger">{{ form.password1.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password2.id_for_label }}" class="form-label">Confirm Password</label>
                        {{ form.password2 }}
                        {% if form.password2.errors %}
                            <div class="text-danger">{{ form.password2.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Register</button>
                    </div>
                </form>
                
                <div class="text-center mt-3">
                    <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- my_jobs.html -->
{% extends 'jobboard/base.html' %}

{% block title %}My Jobs - Job Board{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h2>My Posted Jobs</h2>
    <a href="{% url 'post_job' %}" class="btn btn-success">
        <i class="fas fa-plus"></i> Post New Job
    </a>
</div>

{% if jobs %}
    <div class="row">
        {% for job in jobs %}
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h5 class="card-title">{{ job.title }}</h5>
                            <span class="badge bg-{% if job.is_active %}success{% else %}secondary{% endif %}">
                                {% if job.is_active %}Active{% else %}Inactive{% endif %}
                            </span>
                        </div>
                        
                        <p class="text-muted mb-2">
                            <i class="fas fa-building"></i> {{ job.company.name }}
                        </p>
                        <p class="text-muted mb-2">
                            <i class="fas fa-map-marker-alt"></i> {{ job.location }}
                        </p>
                        <p class="text-muted mb-2">
                            <i class="fas fa-calendar"></i> Posted: {{ job.created_at|date:"M d, Y" }}
                        </p>
                        <p class="text-muted mb-3">
                            <i class="fas fa-clock"></i> Deadline: {{ job.application_deadline|date:"M d, Y" }}
                        </p>
                        
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="text-primary">
                                <i class="fas fa-users"></i> {{ job.applications.count }} applications
                            </span>
                            <div class="btn-group" role="group">
                                <a href="{% url 'job_detail' job.pk %}" class="btn btn-sm btn-outline-primary">View</a>
                                <a href="{% url 'job_applications' job.pk %}" class="btn btn-sm btn-primary">
                                    Applications ({{ job.applications.count }})
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
{% else %}
    <div class="text-center py-5">
        <i class="fas fa-briefcase fa-3x text-muted mb-3"></i>
        <h4 class="text-muted">No jobs posted yet</h4>
        <p class="text-muted">Start by posting your first job!</p>
        <a href="{% url 'post_job' %}" class="btn btn-primary">Post Your First Job</a>
    </div>
{% endif %}
{% endblock %}

<!-- my_applications.html -->
{% extends 'jobboard/base.html' %}

{% block title %}My Applications - Job Board{% endblock %}

{% block content %}
<h2 class="mb-4">My Job Applications</h2>

{% if applications %}
    <div class="row">
        {% for application in applications %}
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h5 class="card-title">{{ application.job.title }}</h5>
                            <span class="badge bg-{% if application.status == 'pending' %}warning{% elif application.status == 'reviewing' %}info{% elif application.status == 'shortlisted' %}primary{% elif application.status == 'interviewed' %}success{% elif application.status == 'hired' %}success{% else %}danger{% endif %}">
                                {{ application.get_status_display }}
                            </span>
                        </div>
                        
                        <p class="text-muted mb-2">
                            <i class="fas fa-building"></i> {{ application.job.company.name }}
                        </p>
                        <p class="text-muted mb-2">
                            <i class="fas fa-map-marker-alt"></i> {{ application.job.location }}
                        </p>
                        <p class="text-muted mb-2">
                            <i class="fas fa-calendar"></i> Applied: {{ application.applied_at|date:"M d, Y" }}
                        </p>
                        <p class="text-muted mb-3">
                            <i class="fas fa-clock"></i> Last updated: {{ application.updated_at|date:"M d, Y" }}
                        </p>
                        
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="badge bg-secondary">{{ application.job.get_job_type_display }}</span>
                            <a href="{% url 'job_detail' application.job.pk %}" class="btn btn-sm btn-outline-primary">View Job</a>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
{% else %}
    <div class="text-center py-5">
        <i class="fas fa-file-alt fa-3x text-muted mb-3"></i>
        <h4 class="text-muted">No applications yet</h4>
        <p class="text-muted">Start applying for jobs to see your applications here!</p>
        <a href="{% url 'job_list' %}" class="btn btn-primary">Browse Jobs</a>
    </div>
{% endif %}
{% endblock %}

<!-- job_applications.html -->
{% extends 'jobboard/base.html' %}

{% block title %}Applications for {{ job.title }} - Job Board{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <div>
        <h2>Applications for {{ job.title }}</h2>
        <p class="text-muted">{{ job.company.name }} • {{ applications.count }} applications</p>
    </div>
    <a href="{% url 'job_detail' job.pk %}" class="btn btn-outline-primary">View Job</a>
</div>

{% if applications %}
    <div class="row">
        {% for application in applications %}
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-3">
                            <div>
                                <h5 class="card-title">{{ application.applicant.first_name }} {{ application.applicant.last_name }}</h5>
                                <p class="text-muted mb-1">{{ application.applicant.email }}</p>
                            </div>
                            <span class="badge bg-{% if application.status == 'pending' %}warning{% elif application.status == 'reviewing' %}info{% elif application.status == 'shortlisted' %}primary{% elif application.status == 'interviewed' %}success{% elif application.status == 'hired' %}success{% else %}danger{% endif %}">
                                {{ application.get_status_display }}
                            </span>
                        </div>
                        
                        <p class="text-muted mb-2">
                            <i class="fas fa-calendar"></i> Applied: {{ application.applied_at|date:"M d, Y H:i" }}
                        </p>
                        
                        <div class="mb-3">
                            <strong>Cover Letter:</strong>
                            <p class="text-muted small">{{ application.cover_letter|truncatewords:30 }}</p>
                        </div>
                        
                        <div class="d-flex justify-content-between align-items-center">
                            {% if application.resume %}
                                <a href="{{ application.resume.url }}" target="_blank" class="btn btn-sm btn-outline-primary">
                                    <i class="fas fa-file-download"></i> Download Resume
                                </a>
                            {% endif %}
                            <div class="btn-group" role="group">
                                <button class="btn btn-sm btn-outline-success" onclick="updateStatus({{ application.id }}, 'shortlisted')">Shortlist</button>
                                <button class="btn btn-sm btn-outline-danger" onclick="updateStatus({{ application.id }}, 'rejected')">Reject</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
{% else %}
    <div class="text-center py-5">
        <i class="fas fa-users fa-3x text-muted mb-3"></i>
        <h4 class="text-muted">No applications yet</h4>
        <p class="text-muted">Applications will appear here when candidates apply for this job.</p>
    </div>
{% endif %}

<script>
function updateStatus(applicationId, status) {
    // This would need to be implemented with AJAX
    // For now, it's just a placeholder
    alert('Status update functionality would be implemented here');
}
</script>
{% endblock %}

# 16 | Resume Builder          | Form to generate PDF resume           | ReportLab/WeasyPrint, PDF export   
# Django Resume Builder - Complete Guide

## Step 1: Create the App

In your terminal, navigate to your Django project directory and run:

```bash
cd projects
python manage.py startapp resume_builder
```

## Step 2: Add App to Settings

In your `projects/settings.py`, add the new app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'resume_builder',  # Add this line
]
```

## Step 3: Install Required Packages

Install the necessary packages for PDF generation:

```bash
pip install reportlab
pip install weasyprint
```

## Step 4: Create Models

In `resume_builder/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}'s Resume"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ])

    def __str__(self):
        return self.name
```

## Step 5: Create Forms

Create `resume_builder/forms.py`:

```python
from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Experience, Education, Skill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone', 'address', 'summary']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your address'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write a brief summary about yourself'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'is_current', 'description']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'grade']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proficiency': forms.Select(attrs={'class': 'form-control'}),
        }

# Create formsets for dynamic forms
ExperienceFormSet = inlineformset_factory(Resume, Experience, form=ExperienceForm, extra=1, can_delete=True)
EducationFormSet = inlineformset_factory(Resume, Education, form=EducationForm, extra=1, can_delete=True)
SkillFormSet = inlineformset_factory(Resume, Skill, form=SkillForm, extra=1, can_delete=True)
```

## Step 6: Create Views

In `resume_builder/views.py`:

```python
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
    pdf_type = request.GET.get('type', 'reportlab')
    
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
```

## Step 7: Create PDF Generation Utils

Create `resume_builder/utils.py`:

```python
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import weasyprint
from django.template.loader import render_to_string

def generate_pdf_reportlab(resume):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        alignment=1,  # Center alignment
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=6,
        textColor=colors.darkblue,
        borderWidth=1,
        borderColor=colors.darkblue,
        borderPadding=5
    )
    
    story = []
    
    # Title
    story.append(Paragraph(resume.full_name, title_style))
    story.append(Spacer(1, 12))
    
    # Contact Info
    contact_info = f"{resume.email} | {resume.phone}"
    story.append(Paragraph(contact_info, styles['Normal']))
    story.append(Paragraph(resume.address, styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Summary
    if resume.summary:
        story.append(Paragraph("SUMMARY", heading_style))
        story.append(Paragraph(resume.summary, styles['Normal']))
        story.append(Spacer(1, 12))
    
    # Experience
    if resume.experiences.exists():
        story.append(Paragraph("EXPERIENCE", heading_style))
        for exp in resume.experiences.all():
            end_date = "Present" if exp.is_current else exp.end_date.strftime("%Y-%m-%d")
            exp_header = f"<b>{exp.job_title}</b> at {exp.company} ({exp.start_date.strftime('%Y-%m-%d')} - {end_date})"
            story.append(Paragraph(exp_header, styles['Normal']))
            story.append(Paragraph(exp.description, styles['Normal']))
            story.append(Spacer(1, 6))
    
    # Education
    if resume.education.exists():
        story.append(Paragraph("EDUCATION", heading_style))
        for edu in resume.education.all():
            end_date = "Present" if edu.is_current else edu.end_date.strftime("%Y-%m-%d")
            edu_header = f"<b>{edu.degree}</b> from {edu.institution} ({edu.start_date.strftime('%Y-%m-%d')} - {end_date})"
            story.append(Paragraph(edu_header, styles['Normal']))
            if edu.grade:
                story.append(Paragraph(f"Grade: {edu.grade}", styles['Normal']))
            story.append(Spacer(1, 6))
    
    # Skills
    if resume.skills.exists():
        story.append(Paragraph("SKILLS", heading_style))
        skills_data = []
        for skill in resume.skills.all():
            skills_data.append([skill.name, skill.proficiency.title()])
        
        skills_table = Table(skills_data, colWidths=[3*inch, 2*inch])
        skills_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(skills_table)
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_pdf_weasyprint(resume):
    html_string = render_to_string('resume_builder/resume_pdf_template.html', {'resume': resume})
    
    html = weasyprint.HTML(string=html_string)
    pdf_buffer = BytesIO()
    html.write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer
```

## Step 8: Create Templates

Create the following directory structure:
```
resume_builder/
    templates/
        resume_builder/
            base.html
            resume_list.html
            resume_form.html
            resume_preview.html
            resume_confirm_delete.html
            resume_pdf_template.html
```

### Base Template (`resume_builder/templates/resume_builder/base.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Resume Builder{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'resume_list' %}">Resume Builder</a>
            <div class="navbar-nav ms-auto">
                {% if user.is_authenticated %}
                    <a class="nav-link" href="{% url 'resume_list' %}">My Resumes</a>
                    <a class="nav-link" href="{% url 'resume_create' %}">Create Resume</a>
                    <a class="nav-link" href="{% url 'admin:logout' %}">Logout</a>
                {% else %}
                    <a class="nav-link" href="{% url 'admin:login' %}">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}
    {% endblock %}
</body>
</html>
```

### Resume List Template (`resume_builder/templates/resume_builder/resume_list.html`):

```html
{% extends 'resume_builder/base.html' %}

{% block title %}My Resumes - Resume Builder{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h1>My Resumes</h1>
    <a href="{% url 'resume_create' %}" class="btn btn-primary">Create New Resume</a>
</div>

{% if resumes %}
    <div class="row">
        {% for resume in resumes %}
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ resume.full_name }}</h5>
                        <p class="card-text">{{ resume.email }}</p>
                        <p class="card-text">
                            <small class="text-muted">Updated: {{ resume.updated_at|date:"M d, Y" }}</small>
                        </p>
                    </div>
                    <div class="card-footer">
                        <a href="{% url 'resume_preview' resume.pk %}" class="btn btn-info btn-sm">Preview</a>
                        <a href="{% url 'resume_edit' resume.pk %}" class="btn btn-warning btn-sm">Edit</a>
                        <a href="{% url 'resume_download_pdf' resume.pk %}" class="btn btn-success btn-sm">Download PDF</a>
                        <a href="{% url 'resume_delete' resume.pk %}" class="btn btn-danger btn-sm">Delete</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
{% else %}
    <div class="text-center">
        <h3>No resumes yet!</h3>
        <p>Create your first resume to get started.</p>
        <a href="{% url 'resume_create' %}" class="btn btn-primary">Create Resume</a>
    </div>
{% endif %}
{% endblock %}
```

## Step 9: Create URLs

Create `resume_builder/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.resume_create, name='resume_create'),
    path('<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('<int:pk>/preview/', views.resume_preview, name='resume_preview'),
    path('<int:pk>/download/', views.resume_download_pdf, name='resume_download_pdf'),
    path('<int:pk>/delete/', views.resume_delete, name='resume_delete'),
]
```

## Step 10: Update Main URLs

In your main `projects/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', include('resume_builder.urls')),
]
```

## Step 11: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 12: Create Superuser and Test

```bash
python manage.py createsuperuser
python manage.py runserver
```

Now you can access your resume builder at `http://127.0.0.1:8000/resume/`

## Next Steps

1. Complete the remaining templates (resume_form.html, resume_preview.html, etc.)
2. Add more styling and JavaScript for better user experience
3. Add user authentication views
4. Implement more advanced PDF styling
5. Add resume templates/themes
6. Add validation and error handling

This gives you a solid foundation for a Django Resume Builder with PDF export functionality using both ReportLab and WeasyPrint!



# P17 : Social Network          | Follow, like, comment system          | Generic Relations, ManyToMany, AJAX    
I'll help you create a social network app with follow, like, and comment functionality in Django! Let's build this step by step.

## Step 1: Create the App

First, create the social network app:

```bash
cd projects
python manage.py startapp social_network
```

## Step 2: Add App to Settings

Add the app to your `INSTALLED_APPS` in `projects/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_network',  # Add this line
]
```

## Step 3: Create Models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return reverse('social_network:profile', kwargs={'username': self.user.username})

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'followed')
    
    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}..."
    
    def get_absolute_url(self):
        return reverse('social_network:post_detail', kwargs={'pk': self.pk})
    
    def get_like_count(self):
        return self.likes.count()
    
    def get_comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.author.username} on {self.post}: {self.content[:30]}..."

class Like(models.Model):
    """Generic Like model that can be used for Posts, Comments, etc."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Generic Foreign Key fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]
    
    def __str__(self):
        return f"{self.user.username} likes {self.content_object}"

# Add generic relation to Post model
from django.contrib.contenttypes.fields import GenericRelation
Post.add_to_class('likes', GenericRelation(Like))
Comment.add_to_class('likes', GenericRelation(Like))
## Step 4: Create Forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Create profile for the user
            Profile.objects.create(user=user)
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'birth_date', 'location', 'website')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control',
                'placeholder': "What's on your mind?"
            }),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2, 
                'class': 'form-control',
                'placeholder': "Write a comment..."
            }),
        }
## Step 5: Create Views
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
## Step 6: Create URLs
from django.urls import path
from . import views

app_name = 'social_network'

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    
    # Main pages
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.user_search, name='search'),
    
    # AJAX endpoints
    path('follow/', views.follow_user, name='follow_user'),
    path('like/', views.like_content, name='like_content'),
    path('comment/', views.add_comment, name='add_comment'),
]
## Step 7: Update Main URLs

Add this to your main `projects/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_network.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Step 8: Update Settings for Media Files

Add these to your `settings.py`:

```python
import os

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Login URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## Step 9: Create Templates Directory Structure

Create these directories:
```
social_network/
├── templates/
│   ├── registration/
│   └── social_network/
```

## Step 10: Create Templates
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Social Network{% endblock %}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        .profile-img {
            width: 40px;
            height: 40px;
            object-fit: cover;
            border-radius: 50%;
        }
        .post-card {
            border: 1px solid #dee2e6;
            border-radius: 10px;
            margin-bottom: 20px;
            background: white;
        }
        .like-btn, .comment-btn {
            border: none;
            background: none;
            color: #6c757d;
            transition: color 0.3s;
        }
        .like-btn:hover, .comment-btn:hover {
            color: #007bff;
        }
        .like-btn.liked {
            color: #dc3545;
        }
        .navbar-brand {
            font-weight: bold;
            color: #007bff !important;
        }
        .comment-section {
            border-top: 1px solid #dee2e6;
            padding-top: 15px;
            margin-top: 15px;
        }
        .comment-item {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body class="bg-light">
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
        <div class="container">
            <a class="navbar-brand" href="{% url 'social_network:home' %}">
                <i class="fas fa-users"></i> SocialNet
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'social_network:home' %}">
                                <i class="fas fa-home"></i> Home
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'social_network:search' %}">
                                <i class="fas fa-search"></i> Search
                            </a>
                        </li>
                    {% endif %}
                </ul>
                
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
                                {% if user.profile.profile_picture %}
                                    <img src="{{ user.profile.profile_picture.url }}" alt="{{ user.username }}" class="profile-img me-1">
                                {% endif %}
                                {{ user.username }}
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="{% url 'social_network:profile' user.username %}">
                                    <i class="fas fa-user"></i> Profile
                                </a></li>
                                <li><a class="dropdown-item" href="{% url 'social_network:edit_profile' %}">
                                    <i class="fas fa-edit"></i> Edit Profile
                                </a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="{% url 'logout' %}">
                                    <i class="fas fa-sign-out-alt"></i> Logout
                                </a></li>
                            </ul>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'social_network:register' %}">Register</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <!-- Messages -->
    {% if messages %}
        <div class="container mt-3">
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        </div>
    {% endif %}

    <!-- Main Content -->
    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>

    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    
    <script>
        // CSRF token for AJAX requests
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');

        // Follow/Unfollow functionality
        $(document).on('click', '.follow-btn', function() {
            const btn = $(this);
            const userId = btn.data('user-id');
            
            $.post('{% url "social_network:follow_user" %}', {
                'user_id': userId,
                'csrfmiddlewaretoken': csrftoken
            })
            .done(function(data) {
                if (data.status === 'followed') {
                    btn.removeClass('btn-primary').addClass('btn-outline-primary');
                    btn.text('Unfollow');
                } else {
                    btn.removeClass('btn-outline-primary').addClass('btn-primary');
                    btn.text('Follow');
                }
                $('.followers-count').text(data.followers_count);
            });
        });

        // Like/Unlike functionality
        $(document).on('click', '.like-btn', function() {
            const btn = $(this);
            const contentTypeId = btn.data('content-type-id');
            const objectId = btn.data('object-id');
            
            $.post('{% url "social_network:like_content" %}', {
                'content_type_id': contentTypeId,
                'object_id': objectId,
                'csrfmiddlewaretoken': csrftoken
            })
            .done(function(data) {
                const icon = btn.find('i');
                const countSpan = btn.find('.like-count');
                
                if (data.status === 'liked') {
                    btn.addClass('liked');
                    icon.removeClass('far').addClass('fas');
                } else {
                    btn.removeClass('liked');
                    icon.removeClass('fas').addClass('far');
                }
                countSpan.text(data.like_count);
            });
        });

        // Add comment functionality
        $(document).on('click', '.add-comment-btn', function() {
            const btn = $(this);
            const postId = btn.data('post-id');
            const commentInput = btn.siblings('.comment-input');
            const content = commentInput.val().trim();
            
            if (!content) {
                alert('Please enter a comment');
                return;
            }
            
            $.post('{% url "social_network:add_comment" %}', {
                'post_id': postId,
                'content': content,
                'csrfmiddlewaretoken': csrftoken
            })
            .done(function(data) {
                if (data.status === 'success') {
                    const commentsContainer = btn.closest('.post-card').find('.comments-container');
                    const newComment = `
                        <div class="comment-item">
                            <div class="d-flex">
                                <div class="flex-shrink-0">
                                    ${data.comment.author_profile_picture ? 
                                        `<img src="${data.comment.author_profile_picture}" alt="${data.comment.author}" class="profile-img">` :
                                        `<div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                            <i class="fas fa-user text-white"></i>
                                        </div>`
                                    }
                                </div>
                                <div class="flex-grow-1 ms-3">
                                    <strong>${data.comment.author}</strong>
                                    <small class="text-muted">${data.comment.created_at}</small>
                                    <p class="mb-0 mt-1">${data.comment.content}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    commentsContainer.append(newComment);
                    commentInput.val('');
                    
                    // Update comment count
                    btn.closest('.post-card').find('.comment-count').text(data.comment_count);
                }
            });
        });
    </script>
    
    {% block extra_js %}
    {% endblock %}
</body>
</html>
{% extends 'social_network/base.html' %}

{% block title %}Home - Social Network{% endblock %}

{% block content %}
<div class="row">
    <!-- Main Content -->
    <div class="col-lg-8">
        <!-- Create Post Form -->
        <div class="card mb-4">
            <div class="card-body">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="d-flex">
                        <div class="flex-shrink-0">
                            {% if user.profile.profile_picture %}
                                <img src="{{ user.profile.profile_picture.url }}" alt="{{ user.username }}" class="profile-img">
                            {% else %}
                                <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                    <i class="fas fa-user text-white"></i>
                                </div>
                            {% endif %}
                        </div>
                        <div class="flex-grow-1 ms-3">
                            {{ post_form.content }}
                            <div class="mt-3">
                                {{ post_form.image }}
                            </div>
                            <div class="mt-3">
                                <button type="submit" class="btn btn-primary">
                                    <i class="fas fa-paper-plane"></i> Post
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <!-- Posts Feed -->
        {% for post in posts %}
            <div class="post-card">
                <div class="card-body">
                    <!-- Post Header -->
                    <div class="d-flex mb-3">
                        <div class="flex-shrink-0">
                            {% if post.author.profile.profile_picture %}
                                <img src="{{ post.author.profile.profile_picture.url }}" alt="{{ post.author.username }}" class="profile-img">
                            {% else %}
                                <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                    <i class="fas fa-user text-white"></i>
                                </div>
                            {% endif %}
                        </div>
                        <div class="flex-grow-1 ms-3">
                            <h6 class="mb-0">
                                <a href="{% url 'social_network:profile' post.author.username %}" class="text-decoration-none">
                                    {{ post.author.get_full_name|default:post.author.username }}
                                </a>
                            </h6>
                            <small class="text-muted">@{{ post.author.username }} • {{ post.created_at|timesince }} ago</small>
                        </div>
                    </div>

                    <!-- Post Content -->
                    <p class="mb-3">{{ post.content }}</p>
                    
                    {% if post.image %}
                        <div class="mb-3">
                            <img src="{{ post.image.url }}" alt="Post image" class="img-fluid rounded">
                        </div>
                    {% endif %}

                    <!-- Post Actions -->
                    <div class="d-flex align-items-center mb-3">
                        <button class="like-btn me-3" data-content-type-id="{{ post_content_type.id }}" data-object-id="{{ post.id }}">
                            <i class="far fa-heart"></i>
                            <span class="like-count">{{ post.get_like_count }}</span>
                        </button>
                        <button class="comment-btn" data-bs-toggle="collapse" data-bs-target="#comments-{{ post.id }}">
                            <i class="far fa-comment"></i>
                            <span class="comment-count">{{ post.get_comment_count }}</span>
                        </button>
                    </div>

                    <!-- Comments Section -->
                    <div class="collapse comment-section" id="comments-{{ post.id }}">
                        <!-- Existing Comments -->
                        <div class="comments-container">
                            {% for comment in post.comments.all|slice:":3" %}
                                <div class="comment-item">
                                    <div class="d-flex">
                                        <div class="flex-shrink-0">
                                            {% if comment.author.profile.profile_picture %}
                                                <img src="{{ comment.author.profile.profile_picture.url }}" alt="{{ comment.author.username }}" class="profile-img">
                                            {% else %}
                                                <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                                    <i class="fas fa-user text-white"></i>
                                                </div>
                                            {% endif %}
                                        </div>
                                        <div class="flex-grow-1 ms-3">
                                            <strong>{{ comment.author.username }}</strong>
                                            <small class="text-muted">{{ comment.created_at|timesince }} ago</small>
                                            <p class="mb-0 mt-1">{{ comment.content }}</p>
                                        </div>
                                    </div>
                                </div>
                            {% endfor %}
                        </div>

                        <!-- Add Comment Form -->
                        <div class="mt-3">
                            <div class="d-flex">
                                <div class="flex-shrink-0">
                                    {% if user.profile.profile_picture %}
                                        <img src="{{ user.profile.profile_picture.url }}" alt="{{ user.username }}" class="profile-img">
                                    {% else %}
                                        <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                            <i class="fas fa-user text-white"></i>
                                        </div>
                                    {% endif %}
                                </div>
                                <div class="flex-grow-1 ms-3">
                                    <div class="input-group">
                                        <textarea class="form-control comment-input" rows="1" placeholder="Write a comment..."></textarea>
                                        <button class="btn btn-outline-primary add-comment-btn" data-post-id="{{ post.id }}">
                                            <i class="fas fa-paper-plane"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {% empty %}
            <div class="text-center py-5">
                <i class="fas fa-users fa-3x text-muted mb-3"></i>
                <h5 class="text-muted">No posts yet!</h5>
                <p class="text-muted">Follow some users to see their posts here, or create your first post above.</p>
            </div>
        {% endfor %}

        <!-- Pagination -->
        {% if posts.has_other_pages %}
            <nav aria-label="Page navigation">
                <ul class="pagination justify-content-center">
                    {% if posts.has_previous %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ posts.previous_page_number }}">Previous</a>
                        </li>
                    {% endif %}
                    
                    {% for num in posts.paginator.page_range %}
                        {% if posts.number == num %}
                            <li class="page-item active">
                                <span class="page-link">{{ num }}</span>
                            </li>
                        {% elif num > posts.number|add:'-3' and num < posts.number|add:'3' %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                            </li>
                        {% endif %}
                    {% endfor %}
                    
                    {% if posts.has_next %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ posts.next_page_number }}">Next</a>
                        </li>
                    {% endif %}
                </ul>
            </nav>
        {% endif %}
    </div>

    <!-- Sidebar -->
    <div class="col-lg-4">
        <div class="card">
            <div class="card-body">
                <h6 class="card-title">Your Profile</h6>
                <div class="d-flex align-items-center">
                    {% if user.profile.profile_picture %}
                        <img src="{{ user.profile.profile_picture.url }}" alt="{{ user.username }}" class="profile-img me-3">
                    {% else %}
                        <div class="profile-img bg-secondary d-flex align-items-center justify-content-center me-3">
                            <i class="fas fa-user text-white"></i>
                        </div>
                    {% endif %}
                    <div>
                        <h6 class="mb-0">{{ user.get_full_name|default:user.username }}</h6>
                        <small class="text-muted">@{{ user.username }}</small>
                    </div>
                </div>
                <div class="mt-3">
                    <a href="{% url 'social_network:profile' user.username %}" class="btn btn-sm btn-outline-primary">View Profile</a>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    // Get content type ID for posts (needed for likes)
    const postContentType = {{ post_content_type.id|default:0 }};
    
    // Update like buttons based on user's likes
    document.addEventListener('DOMContentLoaded', function() {
        // You can add AJAX call here to get user's likes and update buttons
        // For now, we'll handle this in the backend
    });
</script>
{% endblock %}



{% extends 'social_network/base.html' %}

{% block title %}{{ profile.user.get_full_name|default:profile.user.username }} - Social Network{% endblock %}

{% block content %}
<div class="row">
    <div class="col-lg-4">
        <!-- Profile Card -->
        <div class="card">
            <div class="card-body text-center">
                {% if profile.profile_picture %}
                    <img src="{{ profile.profile_picture.url }}" alt="{{ profile.user.username }}" class="rounded-circle mb-3" style="width: 120px; height: 120px; object-fit: cover;">
                {% else %}
                    <div class="bg-secondary rounded-circle d-inline-flex align-items-center justify-content-center mb-3" style="width: 120px; height: 120px;">
                        <i class="fas fa-user fa-3x text-white"></i>
                    </div>
                {% endif %}
                
                <h4>{{ profile.user.get_full_name|default:profile.user.username }}</h4>
                <p class="text-muted mb-3">@{{ profile.user.username }}</p>
                
                {% if profile.bio %}
                    <p class="text-muted">{{ profile.bio }}</p>
                {% endif %}
                
                <!-- Profile Stats -->
                <div class="row text-center mb-3">
                    <div class="col">
                        <strong>{{ posts.count }}</strong>
                        <div class="small text-muted">Posts</div>
                    </div>
                    <div class="col">
                        <strong class="followers-count">{{ followers_count }}</strong>
                        <div class="small text-muted">Followers</div>
                    </div>
                    <div class="col">
                        <strong>{{ following_count }}</strong>
                        <div class="small text-muted">Following</div>
                    </div>
                </div>
                
                <!-- Action Buttons -->
                {% if not is_own_profile %}
                    {% if is_following %}
                        <button class="btn btn-outline-primary follow-btn" data-user-id="{{ profile.user.id }}">
                            Unfollow
                        </button>
                    {% else %}
                        <button class="btn btn-primary follow-btn" data-user-id="{{ profile.user.id }}">
                            Follow
                        </button>
                    {% endif %}
                {% else %}
                    <a href="{% url 'social_network:edit_profile' %}" class="btn btn-primary">
                        <i class="fas fa-edit"></i> Edit Profile
                    </a>
                {% endif %}
                
                <!-- Additional Info -->
                <div class="mt-4 text-start">
                    {% if profile.location %}
                        <div class="mb-2">
                            <i class="fas fa-map-marker-alt text-muted me-2"></i>
                            {{ profile.location }}
                        </div>
                    {% endif %}
                    {% if profile.website %}
                        <div class="mb-2">
                            <i class="fas fa-link text-muted me-2"></i>
                            <a href="{{ profile.website }}" target="_blank" rel="noopener noreferrer">
                                {{ profile.website }}
                            </a>
                        </div>
                    {% endif %}
                    <div class="mb-2">
                        <i class="fas fa-calendar-alt text-muted me-2"></i>
                        Joined {{ profile.created_at|date:"F Y" }}
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-8">
        <!-- Posts -->
        <h5 class="mb-4">
            {% if is_own_profile %}
                Your Posts
            {% else %}
                {{ profile.user.username }}'s Posts
            {% endif %}
        </h5>
        
        {% for post in posts %}
            <div class="post-card">
                <div class="card-body">
                    <!-- Post Header -->
                    <div class="d-flex mb-3">
                        <div class="flex-shrink-0">
                            {% if post.author.profile.profile_picture %}
                                <img src="{{ post.author.profile.profile_picture.url }}" alt="{{ post.author.username }}" class="profile-img">
                            {% else %}
                                <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                    <i class="fas fa-user text-white"></i>
                                </div>
                            {% endif %}
                        </div>
                        <div class="flex-grow-1 ms-3">
                            <h6 class="mb-0">{{ post.author.get_full_name|default:post.author.username }}</h6>
                            <small class="text-muted">{{ post.created_at|timesince }} ago</small>
                        </div>
                    </div>

                    <!-- Post Content -->
                    <p class="mb-3">{{ post.content }}</p>
                    
                    {% if post.image %}
                        <div class="mb-3">
                            <img src="{{ post.image.url }}" alt="Post image" class="img-fluid rounded">
                        </div>
                    {% endif %}

                    <!-- Post Actions -->
                    <div class="d-flex align-items-center mb-3">
                        <button class="like-btn me-3" data-content-type-id="{{ post_content_type.id }}" data-object-id="{{ post.id }}">
                            <i class="far fa-heart"></i>
                            <span class="like-count">{{ post.get_like_count }}</span>
                        </button>
                        <button class="comment-btn" data-bs-toggle="collapse" data-bs-target="#comments-{{ post.id }}">
                            <i class="far fa-comment"></i>
                            <span class="comment-count">{{ post.get_comment_count }}</span>
                        </button>
                        <a href="{% url 'social_network:post_detail' post.id %}" class="btn btn-link btn-sm text-muted ms-auto">
                            View Details
                        </a>
                    </div>

                    <!-- Comments Section -->
                    <div class="collapse comment-section" id="comments-{{ post.id }}">
                        <!-- Existing Comments -->
                        <div class="comments-container">
                            {% for comment in post.comments.all|slice:":3" %}
                                <div class="comment-item">
                                    <div class="d-flex">
                                        <div class="flex-shrink-0">
                                            {% if comment.author.profile.profile_picture %}
                                                <img src="{{ comment.author.profile.profile_picture.url }}" alt="{{ comment.author.username }}" class="profile-img">
                                            {% else %}
                                                <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                                    <i class="fas fa-user text-white"></i>
                                                </div>
                                            {% endif %}
                                        </div>
                                        <div class="flex-grow-1 ms-3">
                                            <strong>{{ comment.author.username }}</strong>
                                            <small class="text-muted">{{ comment.created_at|timesince }} ago</small>
                                            <p class="mb-0 mt-1">{{ comment.content }}</p>
                                        </div>
                                    </div>
                                </div>
                            {% endfor %}
                        </div>

                        <!-- Add Comment Form (only for authenticated users) -->
                        {% if user.is_authenticated %}
                            <div class="mt-3">
                                <div class="d-flex">
                                    <div class="flex-shrink-0">
                                        {% if user.profile.profile_picture %}
                                            <img src="{{ user.profile.profile_picture.url }}" alt="{{ user.username }}" class="profile-img">
                                        {% else %}
                                            <div class="profile-img bg-secondary d-flex align-items-center justify-content-center">
                                                <i class="fas fa-user text-white"></i>
                                            </div>
                                        {% endif %}
                                    </div>
                                    <div class="flex-grow-1 ms-3">
                                        <div class="input-group">
                                            <textarea class="form-control comment-input" rows="1" placeholder="Write a comment..."></textarea>
                                            <button class="btn btn-outline-primary add-comment-btn" data-post-id="{{ post.id }}">
                                                <i class="fas fa-paper-plane"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        {% endif %}
                    </div>
                </div>
            </div>
        {% empty %}
            <div class="text-center py-5">
                <i class="fas fa-pencil-alt fa-3x text-muted mb-3"></i>
                <h5 class="text-muted">
                    {% if is_own_profile %}
                        You haven't posted anything yet!
                    {% else %}
                        {{ profile.user.username }} hasn't posted anything yet!
                    {% endif %}
                </h5>
                {% if is_own_profile %}
                    <p class="text-muted">Share your thoughts with your followers.</p>
                    <a href="{% url 'social_network:home' %}" class="btn btn-primary">Create Your First Post</a>
                {% endif %}
            </div>
        {% endfor %}
    </div>
</div>
{% endblock %}



{% extends 'social_network/base.html' %}

{% block title %}Login - Social Network{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6 col-lg-5">
        <div class="card shadow">
            <div class="card-body p-5">
                <div class="text-center mb-4">
                    <i class="fas fa-users fa-3x text-primary mb-3"></i>
                    <h2>Welcome Back</h2>
                    <p class="text-muted">Sign in to your account</p>
                </div>
                
                <form method="post">
                    {% csrf_token %}
                    
                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}
                    
                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">Username</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                            {{ form.username }}
                        </div>
                        {% if form.username.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.username.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-4">
                        <label for="{{ form.password.id_for_label }}" class="form-label">Password</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            {{ form.password }}
                        </div>
                        {% if form.password.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.password.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary btn-lg">
                            <i class="fas fa-sign-in-alt me-2"></i>Sign In
                        </button>
                    </div>
                </form>
                
                <hr class="my-4">
                
                <div class="text-center">
                    <p class="mb-0">Don't have an account? 
                        <a href="{% url 'social_network:register' %}" class="text-decoration-none">
                            Sign up here
                        </a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .form-control {
        border-left: none;
        border-radius: 0 0.375rem 0.375rem 0;
    }
    .input-group-text {
        background-color: #f8f9fa;
        border-right: none;
    }
</style>
{% endblock %}



{% extends 'social_network/base.html' %}

{% block title %}Register - Social Network{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card shadow">
            <div class="card-body p-5">
                <div class="text-center mb-4">
                    <i class="fas fa-user-plus fa-3x text-primary mb-3"></i>
                    <h2>Join SocialNet</h2>
                    <p class="text-muted">Create your account to get started</p>
                </div>
                
                <form method="post">
                    {% csrf_token %}
                    
                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="{{ form.first_name.id_for_label }}" class="form-label">First Name</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="fas fa-user"></i></span>
                                {{ form.first_name }}
                            </div>
                            {% if form.first_name.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.first_name.errors }}
                                </div>
                            {% endif %}
                        </div>
                        
                        <div class="col-md-6 mb-3">
                            <label for="{{ form.last_name.id_for_label }}" class="form-label">Last Name</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="fas fa-user"></i></span>
                                {{ form.last_name }}
                            </div>
                            {% if form.last_name.errors %}
                                <div class="text-danger small mt-1">
                                    {{ form.last_name.errors }}
                                </div>
                            {% endif %}
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.username.id_for_label }}" class="form-label">Username</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-at"></i></span>
                            {{ form.username }}
                        </div>
                        {% if form.username.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.username.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.email.id_for_label }}" class="form-label">Email</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            {{ form.email }}
                        </div>
                        {% if form.email.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.email.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.password1.id_for_label }}" class="form-label">Password</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            {{ form.password1 }}
                        </div>
                        {% if form.password1.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.password1.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-4">
                        <label for="{{ form.password2.id_for_label }}" class="form-label">Confirm Password</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="fas fa-lock"></i></span>
                            {{ form.password2 }}
                        </div>
                        {% if form.password2.errors %}
                            <div class="text-danger small mt-1">
                                {{ form.password2.errors }}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary btn-lg">
                            <i class="fas fa-user-plus me-2"></i>Create Account
                        </button>
                    </div>
                </form>
                
                <hr class="my-4">
                
                <div class="text-center">
                    <p class="mb-0">Already have an account? 
                        <a href="{% url 'login' %}" class="text-decoration-none">
                            Sign in here
                        </a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .form-control {
        border-left: none;
        border-radius: 0 0.375rem 0.375rem 0;
    }
    .input-group-text {
        background-color: #f8f9fa;
        border-right: none;
    }
</style>
{% endblock %}
