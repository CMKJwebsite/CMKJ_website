from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    """
    产品分类表
    """
    c_category_name = models.CharField(verbose_name='分类名称', max_length=50, default='')
    c_category_alias = models.CharField(verbose_name='分类别名', max_length=50, default='')
    c_parent_catalog = models.CharField(verbose_name='父级分类目录', max_length=50, default='')
    c_category_description = models.CharField(verbose_name='分类描述', max_length=250, default='')
    c_SEO_title = models.CharField(verbose_name='SEO标题', max_length=50, default='')
    c_SEO_Keyword = models.CharField(verbose_name='SEO关键字', max_length=250, default='')
    c_category_thumbnail = models.ImageField(verbose_name='分类缩略图', upload_to='Stage/Project/CMKJ_website/static/images')
    c_PC_advertisement = models.CharField(verbose_name='PC端广告', max_length=250, default='')
    c_Mobile_advertisement = models.CharField(verbose_name='移动端广告', max_length=250, default='')

    class Meta:
        db_table = 'ProductCategory'
        verbose_name_plural = '产品分类表'

    def __str__(self):
        return f"id:{self.id},p_category_name:{self.c_category_name},p_category_alias:{self.c_category_alias}," \
               f"p_parent_catalog:{self.c_parent_catalog},p_category_description:{self.c_category_description}," \
               f"p_SEO_title:{self.c_SEO_title},p_SEO_Keyword:{self.c_SEO_Keyword}," \
               f"P_category_thumbnail:{self.c_category_thumbnail},P_PC_advertisement:{self.c_PC_advertisement}," \
               f"p_Mobile_advertisement:{self.c_Mobile_advertisement}"


class Product(models.Model):
    """
    产品表
    """
    p_name = models.CharField(verbose_name='产品名称', max_length=50, default='')
    p_price = models.DecimalField(verbose_name='产品价格', max_digits=7, decimal_places=2, default=0)
    p_introduction = models.CharField(verbose_name='产品介绍', max_length=250, default='')
    p_details = models.CharField(verbose_name='产品详情', max_length=250, default='')
    p_picture = models.ImageField(verbose_name='产品图片', upload_to='Stage/Project/CMKJ_website/static/images')
    p_category_name = models.ManyToManyField(to=ProductCategory, related_name='category_name')

    class Meta:
        db_table = 'Product'
        verbose_name_plural = '产品表'

    def __str__(self):
        return f"id:{self.id},p_name:{self.p_name},p_type:{self.p_category_name},p_price:{self.p_price}," \
               f"p_introduction:{self.p_introduction},p_details:{self.p_details},p_picture:{self.p_picture}"
