from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import LogInForm


def user_login(request):
	"""用户登陆"""
	if request.method == 'POST':
		user_login_form = LogInForm(data=request.POST)
		if user_login_form.is_valid():
			# .cleaned_data清洗出合法数据
			data = user_login_form.cleaned_data
			# 检验输入的用户名密码是否匹配某个用户
			user = authenticate(username=data['username'], password=data['password'])
			if user:
				# 将用户数据存入session，完成登陆动作
				login(request, user)
				return redirect("article:article_list")
			else:
				return HttpResponse("账号或密码输入有误，请重新输入！")
		else:
			return HttpResponse("账号或密码不合法，请重新输入！")

	elif request.method == 'GET':
		user_login_form = LogInForm()
		context = {'user_login_form': user_login_form}
		return render(request, 'users/login.html', context)
