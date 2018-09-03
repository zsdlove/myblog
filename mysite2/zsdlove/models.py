from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils import timezone
class employeeInfo(models.Model):
    emploee_id=models.CharField(max_length=32)
    emploee_name=models.CharField(max_length=32)
class Category(models.Model):
    name = models.CharField(verbose_name='文章类别', max_length=20)
    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=20)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    #content = models.TextField(verbose_name='正文', default='')
    content=UEditorField(width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",upload_settings={"imageMaxSize":1204000},settings={}, verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='文章类别')
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')
    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name
class friend_link(models.Model):
    link_id=models.CharField(verbose_name='链接序号',max_length=100)
    link_name=models.CharField(verbose_name='链接名字',max_length=100)
    link_address=models.CharField(verbose_name='链接地址',max_length=100)
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
class public_notice(models.Model):
    notice_id=models.CharField(verbose_name='公告序号',max_length=5)
    notice_content=models.CharField(verbose_name='公告内容',max_length=200)
    notice_time=models.DateTimeField(verbose_name='创建时间',default=timezone.now())
    class Meta:
        verbose_name = '站点公告'
        verbose_name_plural = verbose_name