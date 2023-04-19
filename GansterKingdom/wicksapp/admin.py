from django.contrib import admin
from .models import ArmoryData,AdminUsr,heronWicks,Mission

# Register your models here.

class ArmoryDisply(admin.ModelAdmin):
    list_display=('weapon_name','weapon_desc','date_time')


class admindtaDisplay(admin.ModelAdmin):
    list_display=('Admin_name','weapon_desc','date_time')



class herondisplay(admin.ModelAdmin):
    list_display=('lead_title','lead_desc','date_time')


admin.site.register(AdminUsr,admindtaDisplay)
admin.site.register(ArmoryData,ArmoryDisply)
admin.site.register(heronWicks,herondisplay)
admin.site.register(Mission)

