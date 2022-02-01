from .models import Ad
from django.forms import DateInput, ModelForm

class createAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['projectTitle',
                'creatorName',
                'projectDescription',
                'contactDetails',
                'projectStartDate']
        widgets = {
            'projectStartDate': DateInput(attrs={'type': 'date'}),
        }