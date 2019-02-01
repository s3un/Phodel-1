from django.contrib import admin
from .models import Job,States,Lga,Gender,Featured_Jobs,Hot_Jobs
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ViewAdmin(ImportExportModelAdmin):
	pass


class JobsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"jslug": ("Job_title",)}

admin.site.register(Job, JobsAdmin)
admin.site.register(States, ViewAdmin)
admin.site.register(Lga, ViewAdmin)
admin.site.register(Gender)
admin.site.register(Featured_Jobs)
admin.site.register(Hot_Jobs)

