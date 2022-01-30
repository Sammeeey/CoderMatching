from django import forms
from django.forms import DateInput

class createAdForm(forms.Form):
    projectTitle = forms.CharField(label='project title', max_length=100) # label property can actually be left empty: will be generated automatically anyways
    creatorName = forms.CharField(label='creator name', max_length=50)
    projectDescription = forms.CharField(label='project description', max_length=1500)
    contactDetails = forms.CharField(label='contact details', max_length=300)
    # Date and time widgets in django render as text type fields by default - therefore we need a small workaround here to render a field with type="date" - so that we have a nice html date picker -> https://stackoverflow.com/a/60389863
    projectStartDate = forms.DateField(label='project started (date)', widget=DateInput(attrs={'type': 'date'}), required=False)
