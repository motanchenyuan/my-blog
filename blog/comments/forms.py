from django import forms
from .models import Comment

#from blogapp.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name','email','text']

