from django.db import models
from users.models import Address, Crew





class ClientCompany(models.Model):
    avatar_path = models.CharField(max_length=255)
    official_company = models.BooleanField(default=True)
    name_company = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    address = models.ForeignKey(Address, related_name='address', on_delete=models.CASCADE, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    loyalty = models.CharField(max_length=10)
    add_info = models.TextField()

    def __str__(self):
        return self.name
    


class StateType(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)


class ConstructionType(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)


class SpecialWork(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)






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
        blank=True, 
        default=None
    )

class Order(models.Model):
    assingned_crew = models.ForeignKey(
        Crew, 
        related_name='assingned_crew', 
        on_delete=models.CASCADE, 
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

    estimated_cost = models.IntegerField(blank=True, default=0)

    final_cost = models.IntegerField(blank=True, default=0)

    payment_status = models.CharField(max_length=50, blank=False, default='Не оплачено')

    payment_method = models.CharField(max_length=50, blank=True)

    building_address = models.ForeignKey(
        Address, 
        related_name='building_address', 
        on_delete=models.CASCADE, 
        blank=True, 
        default=None
    )







