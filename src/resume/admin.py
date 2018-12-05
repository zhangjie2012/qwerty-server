from django.contrib import admin
from .models import Job, Education


class JobAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'start_dt', 'end_dt', 'title')


admin.site.register(Job, JobAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'start_dt', 'end_dt', 'degree', 'major')


admin.site.register(Education, EducationAdmin)
