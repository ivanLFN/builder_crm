from django.db import models
from users.models import Address





class ClientCompany(models.Model):
    official_company = models.BooleanField(default=True)
    name_company = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    address = models.ForeignKey(Address, related_name='address', on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    loyalty = models.CharField(max_length=10)
    add_info = models.TextField()

    def __str__(self):
        return self.name