from django.contrib import admin

from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    date_hierarchy = 'timeStamp'
    list_display = ('name', 'category', 'visible', 'local', 'display_order', 'timeStamp')
    list_filter = ('visible', 'local')
    search_fields = ('name', 'category', 'content')
    readonly_fields = ['timeStamp', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(CV)
admin.site.register(ContactUs)
