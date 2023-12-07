from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        labels={
            'name': 'StudentName',
            'roll': 'StudentRoll'   
        }
        # widgets={
        #     'name': forms.TextInput(attrs={'class': 'btn btn-primary'}),
        #     'roll':forms.PasswordInput()
        # }
        help_texts={
            'name': 'write your full name',
        }

        error_messages={
            'roll': {'required':'Roll should not be duplicated'},
        }