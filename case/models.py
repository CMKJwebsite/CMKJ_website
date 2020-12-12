from django.db import models

# Create your models here.


class Case(models.Model):
    """
    案例表
    """
    gender_choices = (
        ('s', '软件'),
        ('h', '硬件')
    )
    c_name = models.CharField(verbose_name='案例名称', max_length=50, default='')
    c_category = models.CharField(verbose_name='案例分类', max_length=50, choices=gender_choices, default='')
    c_introduction = models.CharField(verbose_name='客户介绍', max_length=250, default='')
    c_background = models.CharField(verbose_name='项目背景', max_length=250, default='')
    c_challenge = models.CharField(verbose_name='项目挑战', max_length=250, default='')
    c_details = models.TextField(verbose_name='项目详情', max_length=250, default='')
    c_highlights = models.CharField(verbose_name='项目亮点', max_length=250, default='')
    c_reviews = models.CharField(verbose_name='客户评价', max_length=250, default='')
    c_picture = models.ImageField(verbose_name='项目照片', upload_to='Stage/Project/CMKJ_website/static/images')

    class Meta:
        db_table = 'Case'
        verbose_name_plural = '案例表'

    def __str__(self):
        return f"id:{self.id},p_name:{self.c_name},c_category:{self.c_category},c_introduction:{self.c_introduction}," \
               f"c_background:{self.c_background},c_challenge:{self.c_challenge},c_details:{self.c_details}," \
               f"c_highlights:{self.c_highlights},c_reviews:{self.c_reviews},c_picture:{self.c_picture}"
