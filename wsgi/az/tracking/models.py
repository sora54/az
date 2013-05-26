from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Tracking(models.Model):
	tracking_number = models.CharField('运单号',max_length=100)
	remark = models.CharField('备注', max_length=400)
	created_date = models.DateTimeField('创建日期')
	is_closed = models.BooleanField('已完成', default=False)
	
	class Meta:
		verbose_name = '运单'
		verbose_name_plural = '运单'
	
	def __unicode__(self):
		return self.tracking_number
		
	def was_created_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)
#	was_created_recently.admin_order_field = 'created_date'
#	was_created_recently.boolean = True
#	was_created_recently.short_description = '近段时间创建?'
	
class TraceDetail(models.Model):
	tracking = models.ForeignKey(Tracking)
	description = models.CharField('描述', max_length=400)
	created_date = models.DateTimeField('时间')

	class Meta:
		verbose_name = '跟踪明细'
		verbose_name_plural = '跟踪明细'
	
	def __unicode__(self):
		return self.description