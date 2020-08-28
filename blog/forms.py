from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ('name', 'address', 'phone', 'email', 'summary', 'education', 'experience', 'skills',)
