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