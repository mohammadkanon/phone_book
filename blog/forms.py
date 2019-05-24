from django import forms

class AddNumber(forms.Form):
    Name = forms.CharField(max_length=50)
    Number = forms.CharField(max_length=14)