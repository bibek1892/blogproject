from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # or do as, fields=["__all__"]
        fields = ['title', 'contents', 'author', 'image']


class NewsForm(forms.ModelForm):  # data automatically save in model by the model form
    class Meta:
        model = News
        fields = ['title', 'catagory', 'detail', 'author', 'image']


class MessageForm(forms.Form):    # our own forms
    sender = forms.CharField(widget=forms.TextInput())
    mobile = forms.CharField(widget=forms.NumberInput())
    email = forms.CharField(widget=forms.EmailInput())
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['blog']
