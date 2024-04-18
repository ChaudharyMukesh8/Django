from django import forms
class StudentRegistration(forms.Form):

   name = forms.CharField(initial="Mukesh",help_text="this is practice text");email = forms.EmailField()
 # mobile=forms.IntegerField()
  #password = forms.CharField(widget=forms.HiddenInput())
