from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType



class Address(models.Model):
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.country}, {self.region}, {self.city}, {self.street}, {self.house}"


class ClientGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    permissions = models.ManyToManyField(
        'ClientPermission',
        blank=True,
        help_text='The permissions this group has.',
        related_name='client_groups',
    )


class ClientPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        limit_choices_to={'app_label': 'clients'},
    )
    codename = models.CharField(max_length=100)


class CompanyGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    permissions = models.ManyToManyField(
        'CompanyPermission',
        blank=True,
        help_text='The permissions this group has.',
        related_name='company_groups',
    )


class CompanyPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        limit_choices_to={'app_label': 'employees'},
    )
    codename = models.CharField(max_length=100)


class CustomUser(AbstractUser):

    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )

    rating = models.IntegerField(null=True, blank=True)

    phone = models.CharField(max_length=20, null=True, blank=True)

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Не совсем понятен этот момент
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions'
    )


class Crew(models.Model):

    name_crew = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)

    leader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='crew_leader'
    )

    members = models.ManyToManyField(
        CustomUser,
        related_name='crews_joined'
    )

    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name_crew


class TypeSkill(models.Model):

    title_skill = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.title_skill


class Skill(models.Model):

    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='skill_user',
        default=None,
        blank=True
    )

    skill = models.ForeignKey(
        TypeSkill,
        on_delete=models.CASCADE,
        related_name='skill_type',
        default=None,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.created_at


class TypeState(models.Model):

    name_state = models.CharField(
        max_length=50,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name_state


# Работает, уволен, в отпуске
class State(models.Model):

    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='state_user',
        default=None,
        blank=True
    )

    type_state = models.ForeignKey(
        TypeState,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='state_type'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField()

    end_date = models.DateField()

    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.type_state
    


class Departament(models.Model):

    title = models.CharField(max_length=50, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

class TypePosition(models.Model):

    name_position = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField(
        blank=True,
        null=True
    )

    base_salary = models.IntegerField()

    # Требования к кандидатам на позицию
    requirements = models.TextField(default=None)

    # Обязанности, которые необходимо выполнить на данной позиции
    responsibilities = models.TextField(default=None)

    experience_required = models.IntegerField()  # Требуемый опыт работы, в месяцах

    def __str__(self) -> str:
        return self.name_position


class Position(models.Model):

    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='position_user',
        default=None,
        blank=True
    )

    type_position = models.ForeignKey(
        TypePosition,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='position_type'
    )

    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
        related_name='position_departament',
        null=True,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.start_date
