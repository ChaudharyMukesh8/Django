from django import forms
class StudentRegistration(forms.Form):
        #name = forms.CharField(label='Your Name')# To change the label name
        # name = forms.CharField(label_suffix=' ') # to remove the colon 
        #name = forms.CharField(initial='Mukesh')# To give the initial value.
        # name = forms.CharField(required=False) # to remove the required field
        name = forms.CharField(initial= 'Mukesh', disabled=True) # To disabled the input field
        name = forms.CharField(initial='Mukesh',help_text='please do not enter any numeric value')

       
