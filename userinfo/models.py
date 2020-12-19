from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    """
    用户基础信息表
    """
    u_user = models.OneToOneField(User, on_delete=models.CASCADE)
    u_telephone = models.CharField(verbose_name='手机号码', max_length=50, default='', unique=True)

    class Meta:
        db_table = 'UserInfo'
        verbose_name_plural = '用户基础信息表'

    def __str__(self):
        return f"id:{self.id},user:{self.u_user},u_telephone:{self.u_telephone}"
