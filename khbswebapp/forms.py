from django import forms
from .models import *

class StudentRegForm(forms.ModelForm):

    class Meta:
        model = Student_reg
        fields = '__all__'

        widgets = {
            'student_img': forms.ClearableFileInput(attrs={
                'id': 'student-img'
            })
        }


class ParentRegForm(forms.ModelForm):

    class Meta:
        model = Parent_info
        exclude = ['student']

        widgets = {
            'father_img': forms.ClearableFileInput(attrs={
                'id': 'fath-img'
            }),

            'mother_img': forms.ClearableFileInput(attrs={
                'id': 'moth-img'
            })
        }
