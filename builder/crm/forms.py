from django import forms
from crm.models import ClientCompany
from users.forms import AddressForm


class ClientCompanyForm(forms.ModelForm):
    name_company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_info = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ClientCompany
        fields = ('official_company', 'name_company', 'person', 'email', 'phone_number', 'add_info', 'country', 'region')
