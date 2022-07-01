from distutils.log import Log
from django.contrib import admin
from .models import Download, Code
from django.contrib.admin.models import LogEntry

# Register your models here.
admin.site.register(Download)
admin.site.register(Code)
admin.site.register(LogEntry)