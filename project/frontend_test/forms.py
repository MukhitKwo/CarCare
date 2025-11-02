from django import forms

class CarInfoForm(forms.Form):
    car_model = forms.CharField(label='Car Model', max_length=100)

    FUEL_CHOICES = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
        ('Other', 'Other'),
    )
    fuel = forms.ChoiceField(label='Fuel', choices=FUEL_CHOICES)

    tdi = forms.FloatField(label='TDI (if Diesel)', required=False)

    horsepower = forms.IntegerField(label='Horsepower (optional)', required=False, min_value=0)

    TRANSMISSION_CHOICES = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Semi-automatic', 'Semi-automatic'),
        ('CVT', 'CVT'),
        ('Other', 'Other'),
    )
    transmission = forms.ChoiceField(label='Transmission', choices=TRANSMISSION_CHOICES)

    mileage = forms.IntegerField(label='Mileage', min_value=0)

    year_produced = forms.IntegerField(label='Year produced', min_value=1886, max_value=9999)

    vin = forms.CharField(label='VIN (optional)', max_length=17, required=False)

    BODY_TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Wagon', 'Wagon'),
        ('Van', 'Van'),
        ('Pickup', 'Pickup'),
        ('Other', 'Other'),
    )
    body_type = forms.ChoiceField(label='Body type', choices=BODY_TYPE_CHOICES, required=False)

    registration_number = forms.CharField(label='Registration number (optional)', max_length=50, required=False)

    def clean(self):
        cleaned_data = super().clean()
        fuel = cleaned_data.get('fuel')
        tdi = cleaned_data.get('tdi')

        if fuel == 'Diesel' and tdi is None:
            self.add_error('tdi', 'TDI is required for diesel cars.')

        return cleaned_data