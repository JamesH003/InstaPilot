from django import forms
from .models import Airline, Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'image', 'caption', 'airline', 'flight_number',
            'location', 'latitude', 'longitude'
        ]

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/a/72025478
        super().__init__(*args, **kwargs)

        # hide lat/lng by default (auto-generated from map selection)
        self.fields["latitude"].widget = forms.HiddenInput()
        self.fields["longitude"].widget = forms.HiddenInput()
