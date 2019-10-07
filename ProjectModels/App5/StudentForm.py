from django import forms

class StudentForm(forms.Form):
    id=forms.CharField(label="ID",max_length=20)
    name=forms.CharField(label="Name",max_length=20)
    
