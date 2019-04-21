from django.contrib import admin
from .models import NewsModel, comment

# Register your models here
admin.site.register(NewsModel)
admin.site.register(comment)

