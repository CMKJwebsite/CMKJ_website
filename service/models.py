from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Service(models.Model):
    """
    行业服务表
    """
    s_name = models.CharField(verbose_name='行业服务名称', max_length=50, default='')
    s_category = models.CharField(verbose_name='行业服务分类', max_length=50, default='')
    s_introduction = models.CharField(verbose_name='服务介绍', max_length=250, default='')
    s_details = UEditorField(verbose_name='行业服务详情', width=600, height=300, toolbars="full", imagePath="service_images/",
                             filePath="service_files/", upload_settings={"imageMaxSize": 1204000,
                                                                         "fileManagerListPath": 1204000},
                             settings={}, command=None, blank=True)

    class Meta:
        db_table = 'Service'
        verbose_name_plural = '行业服务表'

    def __str__(self):
        return f"id:{self.id},s_name:{self.s_name},s_category:{self.s_category},s_introduction:{self.s_introduction}," \
               f"s_details:{self.s_details}"
