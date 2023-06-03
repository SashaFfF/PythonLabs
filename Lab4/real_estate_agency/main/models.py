from django.db import models


class PropertyType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class ServiceType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class RealEstate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField()
    area = models.DecimalField()
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    purchased = models.BooleanField()


    def __str__(self):
        return self.title


# связь - ?
class Owner(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Deal(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='deals_bought')
    agent = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
