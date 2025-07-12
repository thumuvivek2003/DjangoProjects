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
                recipient_list=['vivek@dexur.com'],
            )
            submitted = True
    else:
        form = ContactForm()
    
    return render(request, 'contactForm/contact.html', {'form': form, 'submitted': submitted})
