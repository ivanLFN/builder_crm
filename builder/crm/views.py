from django.shortcuts import redirect, render
from crm.forms import ClientCompanyForm


def home_page(request):
    return render(request, 'home_page/home_page.html', {})


def clients_page(request):
    pass
    return render(request, 'clients_page/clients_page.html', {})


def updates_page(request):
    return render(request, 'updates_page/updates_page.html', {})


def create_new_client(request):
    if request.method == 'POST':
        form = ClientCompanyForm(request.POST)
        if form.is_valid():
            client_company = form.save()
            return redirect('lients_page')
    else:
        form = ClientCompanyForm()

    return render(request, 'clients_page/create_new_client.html', {'form': form})