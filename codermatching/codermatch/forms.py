from .models import Ad
from django.forms import DateInput, ModelForm

class createAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['adTitle',
                'adPurpose',
                'adDescription',
                'creatorName',
                'contactDetails',
                ]
        widgets = {
            'projectStartDate': DateInput(attrs={'type': 'date'}),
        }