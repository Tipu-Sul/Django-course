from typing import Any
from django import forms
from django.core import validators
    
class contractForm(forms.Form):
    name=forms.CharField(label='User Name',
                          help_text='Name of the contract', 
                          required=False, widget=forms.Textarea(attrs={'id':'textarea', 'class':'form-control', 'placeholder':'Name of the user'}))
    # file=forms.FileField()
    # img=forms.ImageField()
    email=forms.EmailField(label='Email Address')
    age=forms.CharField(label='Age', widget=forms.NumberInput())
    weight=forms.FloatField(label='Weight')
    balance=forms.DecimalField(label='Balance')
    check=forms.BooleanField(label='Check')
    bitrhday=forms.DateField(label='Bitrh Day', widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(label='Appointment', widget=forms.DateInput(attrs={'type':'datetime-local'}) )
    Choices=[('s','Small'), ('m','Medium'), ('l','Long')]
    size=forms.ChoiceField(choices=Choices, label='Size', widget=forms.RadioSelect)
    box=[('P','Peparoni'), ('M','Masrum'), ('B','Beef')]
    piza=forms.MultipleChoiceField(choices=box, label='Piza',widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     Name=forms.CharField(widget=forms.TextInput)
#     Email=forms.CharField(widget=forms.EmailInput)
    # def clean_Name(self):
    #     valueName = self.cleaned_data['Name']
    #     if len(valueName)<10:
    #         raise forms.ValidationError('Please enter a valid name with more than 10 characters')
    #     return valueName

    # def clean_Email(self):
    #     valEmail = self.cleaned_data['Email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('email address must contain .com sign')
    #     return valEmail
    
    # def clean(self):
    #     cleaned_data= super().clean()
    #     valName=self.cleaned_data['Name']
    #     valEmail=self.cleaned_data['Email']
    #     if len(valName)<10:
    #         raise forms.ValidationError('please enter name at least 10 characters')
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('email must contain .com')
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError('enter value at least 10 char')        
class StudentData(forms.Form):
    Name=forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='enter a name at least 10 characters')])
    Email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email address')])
    Age=forms.IntegerField(validators=[validators.MaxValueValidator(40,message='age must be in 40'),validators.MinValueValidator(21,message='age must be upper 21')])
    File=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Enter a valid file path with pdf')])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])


class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['confirm_password']
        val_name=self.cleaned_data['name']
        if val_conpass !=val_pass:
            raise forms.ValidationError('passwords do not match')
        if len(val_name) < 10:
            raise forms.ValidationError('please enter name at least 10 characters')

# class PasswordValidationProject(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_pass = self.cleaned_data['password']
    #     val_conpass = self.cleaned_data['confirm_password']
    #     val_name = self.cleaned_data['name']
    #     if val_conpass != val_pass:
    #         raise forms.ValidationError("Password doesn't match")
    #     if len(val_name) < 15:
    #         raise forms.ValidationError("Name must be at least 15 characters")
        
# class PasswordValidationProject(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    
#     def clean(self):
#         cleaned_data = super().clean()
        
#         val_pass = cleaned_data.get('password')
#         val_conpass = cleaned_data.get('confirm_password')
#         val_name = cleaned_data.get('name')
        
#         if val_conpass and val_pass and val_conpass != val_pass:
#             raise forms.ValidationError("Password doesn't match")
        
#         if val_name and len(val_name) < 15:
#             raise forms.ValidationError("Name must be at least 15 characters")
