from django import forms

from modelapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
     model=Student
     fields=["name",'age','location']
    
        
    
