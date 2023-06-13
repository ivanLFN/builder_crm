from django import forms
from crm.models import ClientCompany


class ClientCompanyForm(forms.ModelForm):
    official_company = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    name_company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_info = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = ClientCompany
        fields = ('official_company', 'name_company', 'person', 'email', 'phone_number,', 'add_info')
