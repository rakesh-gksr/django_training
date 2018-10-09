from django.contrib import admin
from .models import Jobs, AppliedJob
# admin.site.register(Jobs)

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    # fields = ('job_title', 'job_descripttion')
    list_display = ('job_title', 'job_descripttion')
    list_per_page = 2
    search_fields = ('job_title',)
    list_filter = ('job_title',)
    fieldsets = (
        ("Basic", {
            'fields': ('job_title', 'job_descripttion')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('create_on',),
        }),
        ('Advanced options 2', {
            'classes': ('collapse',),
            'fields': ('closed_on',),
        }),
    )
    # Register your models here.
