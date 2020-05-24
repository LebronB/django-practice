from django.db import models
# 导入內建的User模型
from django.contrib.auth.models import User


# 文章数据模型
class Article(models.Model):
	"""博客中文章的相关信息"""
	# 文章作者。on_delete指定数据删除方式，防止关联表的数据不一致。
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	# 文章标题。CharField通常用来存储较短的字符段。max_length为必需参数。
	title = models.CharField(max_length=100)

	# 文章内容。TextField用来保存长文本
	content = models.TextField()

	# 文章创建时间。auto_now_add指定默认填入当前时间
	created = models.DateTimeField(auto_now_add=True)

	# 文章更新时间。auto_now指定默认填入修改时的时间
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		"""使用元类选项为对象添加其他数据"""
		# ordering 对象的排序方法
		# "-created"按创建时间降序排列
		ordering = ['-created']

	def __str__(self):
		"""调用__str__方法时返回文章标题"""
		return self.title



