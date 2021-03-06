from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm): #ModelForm 임을 알려주는 구문.
    class Meta:
        model = Post
        fields = ('title', 'content', 'price', 'rating', 'img' )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'content' , )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)
        widgets = {
            'password': forms.PasswordInput()
        }