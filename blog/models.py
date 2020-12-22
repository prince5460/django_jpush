from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ['-create_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
