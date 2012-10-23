from django.contrib import admin
from models import Applicant, Event

class ApplicantAdmin(admin.ModelAdmin):
  list_display = ('name', 'image_thumb',  'gender', 'studentid', 'school', 'event', 'grade', 'cellphone')
  search_fields = ('name', 'studentid', 'cellphone', )
  list_filter = ('gender', 'school')

class EventAdmin(admin.ModelAdmin):
  list_display = ('name', 'starttime', 'endtime', 'state')
  search_fields = ('name',)
  list_filter = ('state',)

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Event, EventAdmin)
