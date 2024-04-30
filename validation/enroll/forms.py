from django.core import validators #for inbuilt validation
from django import forms

 # For custom validation
def starts_with_m(value):
  if value[0]!= 'm':
    raise forms.ValidationError('Name should start with m')
class StudentRegistration(forms.Form):
      name = forms.CharField(validators=[starts_with_m]) 
      email = forms.EmailField() 
       # this is predefined validation
      #  name = forms.CharField(validators=[validators.MaxLengthValidator(7)]) 
      #  email = forms.EmailField() 
      #  password = forms.CharField(widget = forms.PasswordInput())
     
     # This validation is validate by user itself

      #  def clean(self):
      #   cleaned_data = super().clean()
      #   nameval = self.cleaned_data['name']
      #   valemail = self.cleaned_data['email']
      #   if len(nameval) < 4:
      #     raise forms.ValidationError('Enter more than or equal 4 char')
      #   if len(valemail)<10:
      #      raise forms.validation('should be at least 10 characters')
          

       
