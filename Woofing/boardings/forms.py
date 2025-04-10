from django import forms
from .models import DogBoarding


class BoardingForm(forms.ModelForm):
    class Meta:
        model = DogBoarding
        fields = ['name', 'country', 'city', 'price_per_night', 'description', 'capacity', 'image']

    def clean_city(self):
        city = self.cleaned_data.get("city")
        if not city:
            raise forms.ValidationError("City is required.")
        return city

    def clean_country(self):
        country = self.cleaned_data.get("country")
        if not country:
            raise forms.ValidationError("Country is required.")
        return country
