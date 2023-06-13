from django.shortcuts import redirect, render
from crm.forms import ClientCompanyForm
from users.forms import AddressForm


def home_page(request):
    if request.method == 'POST':
        from_add_order = ClientCompanyForm(request.POST)
        if from_add_order.is_valid():
            
            from_add_order.save()
        return redirect('home_page')
    else:
        from_add_order = ClientCompanyForm()
    return render(request, 'home_page/home_page.html', {'ClientCompanyForm': ClientCompanyForm})


def clients_page(request):
    pass
    return render(request, 'clients_page/clients_page.html', {})


def updates_page(request):
    return render(request, 'updates_page/updates_page.html', {})