from django import forms

# for loop to get list of possible years for the form
years = [x for x in range(1900,2023)]

class dateForm(forms.Form):
    startDate = forms.DateField(widget=forms.SelectDateWidget(years=years), label='Start date')
    endDate = forms.DateField(widget=forms.SelectDateWidget(years=years), label='End date')
