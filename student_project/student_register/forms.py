from django import forms
from .models import StudentUser

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentUser
        fields = ('fullname','number','studentID','level')
        labels = {
            'fullname' : 'Full Name',
            'studentID' : 'Student ID',
            'number' : 'Mobile Number'
        }
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['level'].empty_label = "Select"
        self.fields['number'].required = False