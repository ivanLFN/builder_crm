from django.shortcuts import render


def home_page(request):
    pass
    return render(request, 'home_page/home_page.html', {})


def clients_page(request):
    pass
    return render(request, 'clients_page/clients_page.html', {})


def updates_page(request):
    pass
    return render(request, 'updates_page/updates_page.html', {})