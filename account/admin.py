from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import register, Change_detail
from .models import CustomUser,Pmodel,Pcompany,Gender,images, interest
# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = register
	form=Change_detail
	model=CustomUser

	list_display=['username', 'email', 'first_name', 'last_name','is_model','is_company']

# class ModelsAdmin(admin.ModelAdmin):
# 	prepopulated_fields = {"model_rating": ("id",)}

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Pmodel)
admin.site.register(Pcompany)
admin.site.register(Gender)
admin.site.register(images)
admin.site.register(interest)

