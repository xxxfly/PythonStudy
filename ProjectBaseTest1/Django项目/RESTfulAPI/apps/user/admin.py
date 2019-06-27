from django.contrib import admin
from .models import User,Student,SClass


class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','user_guid','user_name','real_name','mobile','balance','create_date','last_login_date')
    ordering=('user_id',)

class StudentAdmin(admin.ModelAdmin):
    list_display=('s_id','s_name','s_age','s_sex','s_class')
    search_fields=('s_id','s_name')

class SClassAdmin(admin.ModelAdmin):
    list_display=('class_id','class_name','grade')
    search_fields=('class_name',)

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(SClass,SClassAdmin)