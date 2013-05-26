from django.contrib import admin
from tracking.models import Tracking, TraceDetail

class TraceDetailInline(admin.TabularInline):
	model = TraceDetail
	extra = 3

class TrackingAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': [('tracking_number', 'remark'), 'created_date', 'is_closed']}),
		#('时间信息', {'fields': ['created_date'], 'classes':['collapse']}),
	]
	inlines = [TraceDetailInline]
	list_display = ('tracking_number', 'remark', 'created_date', 'is_closed')

	list_filter = ['created_date']
	search_fields = ['tracking_number', 'remark']
	#list_editable = ['remark']

admin.site.register(Tracking, TrackingAdmin)