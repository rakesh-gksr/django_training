from django.contrib import admin
from .models import Example
# admin.site.register(Jobs)

@admin.register(Example)
class ExampleViewAdmin(admin.ModelAdmin):
    # fields = ('job_title', 'job_descripttion')
    pass
    # Register your models here.
