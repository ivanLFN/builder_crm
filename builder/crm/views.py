from django.shortcuts import render


def home_page(request):
    pass
    return render(request, 'home_page/home_page.html', {})