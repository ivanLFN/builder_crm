from typing import Any
from django.db import models
from users.models import Address, Crew

class ClientCompany(models.Model):
    avatar_path = models.CharField(max_length=255, blank=True)
    official_company = models.BooleanField(default=True, blank=True)
    name_company = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    loyalty = models.CharField(max_length=10)
    add_info = models.TextField()
    country = models.CharField(max_length=255, null=True, default=None)
    region = models.CharField(max_length=255, null=True, default=None)
    city = models.CharField(max_length=255, null=True, blank=True, default=None)
    street = models.CharField(max_length=255, null=True, blank=True, default=None)
    house = models.CharField(max_length=255, null=True, blank=True, default=None)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, default=0)

    def __str__(self):
        return self.name_company
    
class StateType(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    
class ConstructionType(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title

class SpecialWork(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title

class CurrentReport(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
  
class ImageDb(models.Model):
    path_img = models.CharField(max_length=255)
    owner = models.ForeignKey(
        CurrentReport, 
        related_name='owner', 
        on_delete=models.CASCADE, 
        blank=True
    )

class Order(models.Model):
    client = models.ForeignKey(
        ClientCompany,
        related_name='client', 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        default=None
    )

    assingned_crew = models.ForeignKey(
        Crew, 
        related_name='assingned_crew', 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        default=None
    )

    create_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()

    state_order = models.ForeignKey(
        StateType, 
        related_name='state_order', 
        on_delete=models.CASCADE, 
        blank=True, 
        default=None
    )

    construction_type = models.ForeignKey(
        ConstructionType, 
        related_name='construction_type', 
        on_delete=models.CASCADE, 
        blank=True, 
        default=None
    )

    special_work = models.ForeignKey(
        SpecialWork, 
        related_name='special_work', 
        on_delete=models.CASCADE, 
        blank=True, 
        default=None
    )

    title_order = models.CharField(max_length=255)

    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    final_cost = models.IntegerField(blank=True, default=0)

    payment_status = models.CharField(max_length=50, blank=False, default='Не оплачено')

    payment_method = models.CharField(max_length=50, blank=True)

    building_address = models.ForeignKey(
        Address, 
        related_name='building_address', 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        default=None
    )

    description = models.TextField(blank=True)







