from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
gender_choices = [
    ('Male','Male'),
    ('Female','Female'),
]
class user_signup(UserCreationForm):
    # address = forms.CharField(max_length=100,required = True)
    # gender = forms.ChoiceField(choices = gender_choices,required = True)
    # nid = forms.IntegerField(label = 'National Identity Card Number',required = True) 
    # phone_number = forms.CharField(max_length=11,required = True) 
    # nid_pic = forms.ImageField(label = 'National Identity Card Photo')
    # profile_pic = forms.ImageField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name']
                #  ,'email','address','gender','nid','phone_number','nid_pic','profile_pic']           
        
     