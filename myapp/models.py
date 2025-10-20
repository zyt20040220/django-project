from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目列表'
    
    def __str__(self):
        return self.title
