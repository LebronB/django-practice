from django import forms

from . import models


class ArticleForm(forms.ModelForm):
	"""创建新文章的表单"""
	class Meta:
		# 指明数据来源
		model = models.Article
		# 定义表单包含的字段
		fields = ('title', 'content')