"""配置article的urls"""
from django.urls import re_path, path
from . import views

# 正在部署的app(django 2.0之后必须配置app_name)
app_name = 'article'

urlpatterns = [
	# 首页文章列表
	path('article_list/', views.article_list, name='article_list'),
	# 文章详情
	path('article_detail/<int:article_id>/', views.article_detail, name='article_detail'),
	# 创建新文章的页面
	path('create/', views.article_create, name='article_create'),
	# 安全删除文章
	path(
		'article_safe_delete/<int:article_id>/',
		views.article_safe_delete,
		name='article_safe_delete'
	),
	# 修改文章
	path('update/<int:article_id>/', views.article_update, name='article_update'),
]