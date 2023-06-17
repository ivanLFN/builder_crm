from django import forms
from crm.models import ClientCompany, ConstructionType, SpecialWork, Order, StateType
from users.forms import AddressForm


class ClientCompanyForm(forms.ModelForm):
    name_company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_info = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    loyalty = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ClientCompany
        fields = ('official_company', 'name_company', 'person', 'email', 'phone_number', 'add_info', 'country', 'region', 'loyalty')




class OrderForm(forms.ModelForm):
    title_order = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    construction_type = forms.ModelChoiceField(queryset=ConstructionType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    special_work = forms.ModelChoiceField(queryset=SpecialWork.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    state_order = forms.ModelChoiceField(queryset=StateType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    end_at = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    client = forms.ModelChoiceField(queryset=ClientCompany.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    estimated_cost = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = Order
        fields = ('end_at', 'construction_type', 'special_work', 'state_order', 'title_order', 'estimated_cost')
