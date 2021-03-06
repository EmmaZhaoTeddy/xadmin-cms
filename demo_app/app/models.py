#coding:utf-8
from django.db import models

class Category(models.Model):
    name = models.CharField(u"名称", max_length=64)
    parent = models.ForeignKey('self', verbose_name=u'父类别', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name=u'类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u"标题", max_length=200)
    date = models.DateField(u"发布时间")
    content = models.TextField(u"内容", null=True, blank=True)
    categories = models.ManyToManyField('Category', null=True, blank=True)

    class Meta:
        verbose_name=u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
