from django import forms


class AboutForm(forms.Form):
    email = forms.EmailField()
    contact = forms.CharField(max_length=10)
