# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import Member

  
# create a ModelForm 
class MemberModelForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Member
        fields = "__all__"

    

class MemModelForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Member
        fields = ['first_name', 'last_name', 'age']