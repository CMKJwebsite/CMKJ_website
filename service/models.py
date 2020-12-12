from django.db import models

# Create your models here.


class Service(models.Model):
    """
    行业服务表
    """
    s_name = models.CharField(verbose_name='行业服务名称', max_length=50, default='')
    s_category = models.CharField(verbose_name='行业服务分类', max_length=50, default='')
    s_introduction = models.CharField(verbose_name='服务介绍', max_length=250, default='')
    s_details = models.TextField(verbose_name='服务详情', max_length=250, default='')

    class Meta:
        db_table = 'Service'
        verbose_name_plural = '行业服务表'

    def __str__(self):
        return f"id:{self.id},s_name:{self.s_name},s_category:{self.s_category},s_introduction:{self.s_introduction}," \
               f"s_details:{self.s_details}"
