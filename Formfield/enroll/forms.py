from django import forms
class StudentRegistration(forms.Form):
       name = forms.CharField(min_length=5,max_length=20,empty_value='Mukesh' ,error_messages={'required':'Please Enter Your Name:'}) 
       # for integer field
       roll = forms.IntegerField(min_value=5)
       # For Decimal values
       price = forms.DecimalField(min_value=4,max_digits=4,decimal_places=1)
       rate = forms.FloatField(min_value=4)
       comment = forms.SlugField()
       email = forms.EmailField(min_length=5, max_length=20)
       website = forms.URLField(min_length=5, max_length=20)
       password = forms.CharField(min_length=5,max_length=20,widget = forms.PasswordInput())
       description = forms.CharField(widget=forms.Textarea)
       feedback = forms.CharField(min_length= 5, max_length=20,
       widget = forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))
       notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))

       agree = forms.BooleanField(label_suffix=' ', label='I agree') 

       

       
