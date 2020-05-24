from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# 从moderls.py中导入类
from .models import Article
from .forms import ArticleForm


# 视图函数
def article_list(request):
	"""首页的文章列表"""
	# 从Article类取出所有文章
	articles = Article.objects.all()
	# 控制首页文章摘要的长度在20字符以下
	for article in articles:
		if len(article.content) > 20:
			article.content = article.content[:20] + "..."
	# 需要传递给模板的对象
	context = {'articles': articles}
	# render：载入模板（template）并返回context
	return render(request, 'article/article_list.html', context)


def article_detail(request, article_id):
	"""阅读文章"""
	# 取出由article_id确认的一篇文章
	article = Article.objects.get(id=article_id)

	# 将markdown语法渲染成html样式

	# 传递给模板的对象
	context = {'article': article}

	return render(request, 'article/article_detail.html', context)


def article_create(request):
	"""创建新文章"""
	# 判断是否为提交数据
	if request.method == 'POST':
		# 处理提交的表单数据
		article_form = ArticleForm(data=request.POST)
		# 判断表单是否满足模型要求
		if article_form.is_valid():
			new_article = article_form.save(commit=False)
			# 先将作者指定为管理员用户
			new_article.author = User.objects.get(id=1)
			# 保存到数据库中
			new_article.save()

			# 返回到文章列表
			return redirect('article:article_list')
		# 若数据不合法
		else:
			return HttpResponse('表单内容有误，请重新输入！')
	# 若用户获取数据
	else:
		# 创建新表单
		article_form = ArticleForm()
		# 赋值给上下文
		context = {'article_form': article_form}
		return render(request, 'article/create.html', context)


def article_safe_delete(request, article_id):
	"""使用隐藏表单安全地删除文章"""
	if request.method == 'POST':
		# 取出由article_id确认的一篇文章
		article = Article.objects.get(id=article_id)
		# 删除该文章
		article.delete()
		# 返回文章列表
		return redirect("article:article_list")
	else:
		return HttpResponse('仅允许post请求')


def article_update(request, article_id):
	"""修改现有的文章"""
	article = Article.objects.get(id=article_id)
	if request.method == 'POST':
		article_form = ArticleForm(data=request.POST)
		if article_form.is_valid():
			article.title = request.POST['title']
			article.content = request.POST['content']
			article.save()
			return redirect("article:article_detail", article_id=article_id)
		else:
			return HttpResponse("表单信息有误，请重新填写")

	else:
		article_form = ArticleForm()
		context = {'article': article, 'article_form': article_form}
		return render(request, "article/update.html", context)