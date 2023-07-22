from django.shortcuts import redirect, render, get_object_or_404
from crm.forms import ClientCompanyForm, OrderForm, Order, OrderEditForm
from django.contrib import messages

COUNT_ITEMS_SHOW = 10

def home_page(request):
    orders = Order.objects.all().order_by('end_at')

    filters_orders = [
        {
            'title': 'По времени',
            'content': list(orders)[:COUNT_ITEMS_SHOW]
        },

        {
            'title': 'Высокий приоритет',
            'content': [order for order in orders if order.client.loyalty == '1']
        },

        {
            'title': 'В процессе',
            'content': [order for order in orders if order.state_order.title == 'В работе']
        },

        {
            'title': 'Выполненные',
            'content': [order for order in orders if order.state_order.title == 'Выполнен']
        }
    ]

    data = {
        'orders': orders,
        'filters_orders': filters_orders
    }

    return render(request, 'home_page/home_page.html', data)

def clients_page(request):
    return render(request, 'clients_page/clients_page.html', {})

def updates_page(request):
    return render(request, 'updates_page/updates_page.html', {})

def create_new_client(request):
    if request.method == 'POST':
        form = ClientCompanyForm(request.POST)
        if form.is_valid():
            client_company = form.save()
            messages.success(request, 'Клиент успешно создан!')
            return redirect('clients_page')
    else:
        form = ClientCompanyForm()

    return render(request, 'clients_page/create_new_client.html', {'form': form})

def create_new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = form.cleaned_data['client']
            order.save()
            messages.success(request, 'Заказ успешно создан!')
            return redirect('home_page')
    else:
        form = OrderForm()

    return render(request, 'home_page/create_new_order.html', {'form': form})

def table_orders_page(request):
    return render(request, 'home_page/table_orders_page.html', {})

def search_view(request):
    title = request.GET.get('keywords', '')
    results = Order.objects.filter(title_order__icontains=title)
    return render(request, 'home_page/search_results.html', {'results': results})

def result_detail(request, result_id):
    order = get_object_or_404(Order, id=result_id)
    form = None
    if request.method == 'POST':
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('table_orders_page')
        else:
            form = OrderEditForm(instance=order)
    return render(request, 'home_page/result_detail.html', {'form': form, 'order': order})


