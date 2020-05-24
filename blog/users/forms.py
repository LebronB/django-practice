from django import forms
from django.contrib.auth.models import User


#定义登陆表单类
class LogInForm(forms.Form):
	"""用户登陆填写的表单"""
	username = forms.CharField()
	password = forms.CharField()
