from django.db import models
from django.contrib.auth.models import AbstractUser


class Departament(models.Model):

    title = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):

    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Position(models.Model):

    title = models.CharField(max_length=50)

    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE
    )

    base_salary = models.IntegerField()

    description = models.TextField(default=None)

    # Требования к кандидатам на позицию
    requirements = models.TextField(default=None)

    # Обязанности, которые необходимо выполнить на данной позиции
    responsibilities = models.TextField(default=None)

    created_at = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField(
        widget=models.DateInput(attrs={'type': 'date'})
    )

    end_date = models.DateField(
        widget=models.DateInput(attrs={'type': 'date'})
    )

    skills_required = models.ManyToManyField(
        Skill,
        on_delete=models.CASCADE
    )

    experience_required = models.IntegerField()  # Требуемый опыт работы, в месяцах

    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


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


# Работает, уволен, в отпуске
class State(models.Model):

    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField(
        widget=models.DateInput(attrs={'type': 'date'})
    )

    end_date = models.DateField(
        widget=models.DateInput(attrs={'type': 'date'})
    )

    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class CustomUser(AbstractUser):

    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )

    positions = models.ManyToManyField(
        Position,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    phone = models.CharField(max_length=20)

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

    dismissal_at = models.DateTimeField(default=None)

    states = models.ManyToManyField(
        State,
        on_delete=models.CASCADE
    )

    # notes = models.ManyToManyField(Note)

    skills = models.ManyToManyField(Skill)

    is_client = models.BooleanField(default=False)


class Crew(models.Model):

    name_crew = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)

    leader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    members = models.ManyToManyField(
        CustomUser,
        related_name='crews_joined'
    )

    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name_crew
