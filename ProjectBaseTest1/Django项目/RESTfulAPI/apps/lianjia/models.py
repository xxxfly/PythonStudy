from django.db import models

# Create your models here.

class whlianjiachengjiao(models.Model):
    """
    武汉链家成交数据
    """

    ID = models.AutoField(primary_key=True, verbose_name='ID')
    url = models.CharField(max_length=512, verbose_name='详情Url')
    title = models.CharField(max_length=512, verbose_name='标题')
    houseArea = models.CharField(max_length=32, verbose_name='房屋区域')
    communityName = models.CharField(max_length=512, verbose_name='社区名称')
    houseType = models.CharField(max_length=32, verbose_name='房屋类型')
    houseSize = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='房屋面积')
    dealPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='交易价格')
    unitPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='单价')
    dealDate = models.DateField(verbose_name='交易日期')
    onPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='挂牌价格')
    dealCycleDay = models.IntegerField(verbose_name='交易周期')
    houseDirection = models.CharField(max_length=32, verbose_name='朝向')
    houseDecoration = models.CharField(max_length=32, verbose_name='装修情况')
    houseFlood = models.CharField(max_length=64, verbose_name='楼层和年代')

    class Meta:
        verbose_name = '武汉链家成交数据'
        verbose_name_plural = verbose_name


class whlianjiaershoufang(models.Model):
    """
    武汉二手房数据
    """

    ID = models.AutoField(primary_key=True, verbose_name='ID')
    url = models.CharField(max_length=512, verbose_name='详情Url')
    title = models.CharField(max_length=512, verbose_name='标题')
    onPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='挂牌价格')
    unitPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='单价')
    houseArea = models.CharField(max_length=32, verbose_name='房屋区域')
    communityName = models.CharField(max_length=512, verbose_name='社区名称')
    houseType = models.CharField(max_length=32, verbose_name='房屋类型')
    houseSize = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='房屋面积')
    houseDirection = models.CharField(max_length=32, verbose_name='朝向')
    houseDecoration = models.CharField(max_length=32, verbose_name='装修情况')
    houseFlood = models.CharField(max_length=64, verbose_name='楼层和年代')
    housePosition = models.CharField(max_length=64, verbose_name='位置')
    visit = models.IntegerField(verbose_name='交易周期')
    onDate = models.DateField(verbose_name='交易日期')

    class Meta:
        verbose_name = '武汉链家二手房数据'
        verbose_name_plural = verbose_name
