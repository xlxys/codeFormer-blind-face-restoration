# from django import forms

# class UserImageForm(forms.Form):
#     bgEnhance = forms.BooleanField(required=False)
#     upsample = forms.BooleanField(required=False)
#     fidility = forms.FloatField(max_value = 1, min_value = 0, step_size = 0.1)
#     file = forms.FileField()


from .models import *  
from django import forms  
  
  
# class UserImage(forms.ModelForm):  
#     class meta:  
#         models = UploadImage  
#         fields = '__all__'  

class UploadForm(forms.ModelForm):


    bgEnhance = forms.BooleanField(label='Background Enhance',required=False)
    upsample = forms.BooleanField(label='Up Sample',required=False)
    fidility = forms.FloatField(min_value = 0, max_value = 1, label='Fidility', initial= 0.5,widget=forms.NumberInput(attrs={'class': 'custom','type': 'range', 'min': '0', 'max': '1', 'step': '0.1'}))
    Img = forms.ImageField(label='Image')
    
    class Meta:
        model = Image
        fields = '__all__'  
        label_suffix = ':'