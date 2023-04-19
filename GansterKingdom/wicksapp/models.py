from django.db import models

# Create your models here.
class AdminUsr(models.Model):
    Admin_name=models.CharField(max_length=50)
    weapon_desc=models.TextField()
    weapon_img=models.ImageField(upload_to='admin_conf/',blank=True, null=True)
    date_time=models.DateField(auto_created=True,null=True)

    

    def __str__(self):
        return self.Admin_name




class ArmoryData(models.Model):
    weapon_name=models.CharField(max_length=50)
    weapon_desc=models.TextField()
    url=models.CharField(max_length=100)
    weapon_img=models.ImageField(upload_to='admin_conf_data/',blank=True, null=True)
    admin_id=models.ForeignKey(AdminUsr,on_delete=models.CASCADE)
    date_time=models.DateField(auto_created=True,null=True)
    
    def __str__(self):
        return self.weapon_name
    

class heronWicks(models.Model):
    lead_title=models.CharField(max_length=40)
    lead_desc=models.TextField()
    lead_img=models.ImageField(upload_to='Wicks_heron/',blank=True,null=True)
    admin_id=models.ForeignKey(AdminUsr,on_delete=models.CASCADE)
    date_time=models.DateField(auto_created=True,null=True)
    
    def __str__(self):
        return self.lead_title



class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='mission_backgrounds/')
    audio_file = models.FileField(upload_to='mission_audio/')

    def __str__(self):
        return self.title


