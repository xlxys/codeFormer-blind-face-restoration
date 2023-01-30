from django.db import models  
  
# class UploadImage(models.Model):  
#     bgEnhance = models.BooleanField()
#     upsample = models.BooleanField()
#     fidility = models.FloatField(max_length=1)
#     image = models.ImageField(upload_to='images')  
  


class Image(models.Model):
    bgEnhance = models.BooleanField()
    upsample = models.BooleanField()
    fidility = models.FloatField(max_length=1)
    Img = models.ImageField(upload_to='images/')