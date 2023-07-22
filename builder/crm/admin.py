from django.contrib import admin
from crm.models import Order, ClientCompany, StateType, ConstructionType, SpecialWork

admin.site.register(Order)
admin.site.register(ClientCompany)
admin.site.register(StateType)
admin.site.register(ConstructionType)
admin.site.register(SpecialWork)
