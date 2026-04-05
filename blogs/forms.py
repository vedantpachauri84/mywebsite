from django import forms
from .models import Comment, Post,Ideas


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'useremail', 'text']
        labels={"username":"Name"}
class PostForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields=['name','title','description']
