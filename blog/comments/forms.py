from django import forms
from .models import Comment
#以下为用户注册导入
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name','email','text']
#注册部分代码
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
