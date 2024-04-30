from django.core import validators
from django import forms
class StudentRegistration(forms.Form):
   name = forms.CharField()
   email=forms.EmailField()
   password = forms.CharField(widget = forms.passwordInput)
   rpassword = forms.CharField(widget= forms.PasswordInput)
   def clean(self):
    cleaned_data = super().clean()
    valpw = self.cleaned_data['password']
    valrpw=self. cleaned_data['rpassword']
    if valpw != valrpw:
      raise forms.ValidationError('Password not matched')
