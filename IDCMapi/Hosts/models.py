from django.db import models
import uuid

# Create your models here.


class Host(models.Model):
    '''
    物理服务器类
    '''

    # 服务器的基本情况
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, db_column='id',verbose_name='服务器ID')
    name = models.CharField(max_length=50, unique=True,
                            blank=False, db_column='name',verbose_name='服务器名称')
    vendor = models.CharField(max_length=50, blank=False, db_column='vendor',verbose_name='服务器厂商')
    serial_number = models.CharField(
        max_length=50, blank=False, db_column='serial_number',verbose_name='服务器序列号')
    model = models.CharField(max_length=50, blank=False, db_column='model',verbose_name='服务器型号')
    warranty = models.BooleanField(
        null=False, blank=False, db_column='warranty', default=False,verbose_name='服务器是否在保')

    # 网卡相关
    network_adapter_speed = models.CharField(
        max_length=50, blank=True, db_column='network_adapter_speed',verbose_name='服务器网卡速率')
    network_adapters = models.PositiveSmallIntegerField(
        blank=True, db_column='network_adapters', null=True,verbose_name='服务器网卡数量')

    # 运算相关
    processor_type = models.CharField(
        max_length=50, blank=True, db_column='processor_type',verbose_name='服务器处理器型号')
    cpu_cores = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='cpu_cores',verbose_name='处理器核心数')
    hyperthreading = models.BooleanField(
        blank=True, db_column='hyperthreading', default=False,verbose_name='处理器是否支持超线程')
    memory = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='memory',verbose_name='服务器内存大小')

    # 存储相关
    storage_capacity = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='storage_capacity',verbose_name='存储容量')
    disk_type = models.CharField(
        max_length=50, blank=True, db_column='disk_type',verbose_name='磁盘类型')
    disk_number = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='disk_number',verbose_name='磁盘数量')
    raid_type = models.CharField(
        max_length=50, blank=True, db_column='raid_type',verbose_name='磁盘RAID')

    def __str__(self):
        return self.host_name

    class Meta:
        db_table = 'host'
