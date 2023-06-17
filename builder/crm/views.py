from django.shortcuts import redirect, render
from crm.forms import ClientCompanyForm, OrderForm, Order
from django.contrib import messages

COUNT_ITEMS_SHOW = 5


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
    pass
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
            order = form.save(commit=False)  # Создаем экземпляр Order без сохранения в базу данных
            order.client = form.cleaned_data['client']  # Устанавливаем значение поля client на основе данных из формы
            order.save()
            messages.success(request, 'Заказ успешно создан!')
            return redirect('home_page')
    else:
        form = OrderForm()

    return render(request, 'home_page/create_new_order.html', {'form': form})