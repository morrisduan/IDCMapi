from django.db import models
import uuid

# Create your models here.


class Host(models.Model):
    '''
    物理服务器类
    '''

    # 服务器的基本情况
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, db_column='id')
    name = models.CharField(max_length=50, unique=True,
                            blank=False, db_column='name')
    vendor = models.CharField(max_length=50, blank=False, db_column='vendor')
    serial_number = models.CharField(
        max_length=50, blank=False, db_column='serial_number')
    model = models.CharField(max_length=50, blank=False, db_column='model')
    warranty = models.BooleanField(
        null=False, blank=False, db_column='warranty', default=False)

    # 网卡相关
    network_adapter_speed = models.CharField(
        max_length=50, blank=True, db_column='network_adapter_speed')
    network_adapters = models.PositiveSmallIntegerField(
        blank=True, db_column='network_adapters', null=True)

    # 运算相关
    processor_type = models.CharField(
        max_length=50, blank=True, db_column='processor_type')
    cpu_cores = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='cpu_cores')
    hyperthreading = models.BooleanField(
        blank=True, db_column='hyperthreading', default=False)
    memory = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='memory')

    # 存储相关
    storage_capacity = models.CharField(
        max_length=50, blank=True, db_column='storage_capacity')
    disk_type = models.CharField(
        max_length=50, blank=True, db_column='disk_type')
    disk_number = models.PositiveSmallIntegerField(
        blank=True, null=True, db_column='disk_number')
    raid_type = models.CharField(
        max_length=50, blank=True, db_column='raid_type')

    def __str__(self):
        return self.host_name

    class Meta:
        db_table = 'host'
