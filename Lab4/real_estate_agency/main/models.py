from django.db import models
from django.urls import reverse

class PropertyType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class ServiceType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуг'


class RealEstate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    area = models.DecimalField(decimal_places=2, max_digits=5)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    purchased = models.BooleanField()

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property', kwargs={'property_id': self.pk})

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        ordering = ['title', 'price']


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_details = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_details = models.CharField(max_length=100)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)


    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Deal(models.Model):
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    agent = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
