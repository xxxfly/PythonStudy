from django.contrib import admin
from .models import whlianjiaershoufang,whlianjiachengjiao

class whlianjiachengjiaoAdmin(admin.ModelAdmin):
    list_display=('url','title','houseArea','houseSize','dealPrice','unitPrice','dealDate')
    ordering=('dealPrice',)
    search_fields=('title','houseArea')

class whlianjiaershoufangAdmin(admin.ModelAdmin):
    list_display=('url','title','houseArea','houseSize','onPrice','unitPrice','onDate')
    ordering=('onDate',)
    search_fields=('title','houseArea')



# Register your models here.
admin.site.register(whlianjiaershoufang, whlianjiaershoufangAdmin)
admin.site.register(whlianjiachengjiao, whlianjiachengjiaoAdmin)
