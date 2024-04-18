from django import forms
class StudentRegistration(forms.Form):
        #name = forms.CharField(label='Your Name')# To change the label name
        # name = forms.CharField(label_suffix=' ') # to remove the colon 
        #name = forms.CharField(initial='Mukesh')# To give the initial value.
        # name = forms.CharField(required=False) # to remove the required field
        #name = forms.CharField(widget=forms.PasswordInput)# for password type input
       # name = forms.CharField(widget=forms.HiddenInput) # for hide the input field
       #name = forms.CharField(widget=forms.Textarea)# for textarea type input box
        # name = forms.CharField(widget=forms.CheckboxInput)  # for checkbox input
       # name = forms.CharField(widget=forms.FileInput) # for file type input
       name = forms.CharField()
       email = forms.EmailField() # for taking the class and id name...

       

       
