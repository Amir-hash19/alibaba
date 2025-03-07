from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField(unique=True, max_length=12)
    national_id = models.CharField(max_length=11 ,unique=True)
    email = models.EmailField(null=True, blank=True)
    age = models.PositiveIntegerField()



class Bus(models.Model):
    origin = models.CharField(max_length=50)
    destinations = models.CharField(max_length=50)
    back_forth = models.BooleanField(default=False)
    resarve_status = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    situation = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    capicity = models.PositiveIntegerField()
    company_name = models.CharField(max_length=100)


class Airplane(models.Model):
    origin = models.CharField(max_length=50)
    destinations = models.CharField(max_length=50)
    back_forth = models.BooleanField(default=False)
    resarve_status = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    capicity = models.PositiveIntegerField()
    number_fly = models.PositiveIntegerField()
    situation = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)


class Train(models.Model):
    origin = models.CharField(max_length=50)
    destinations = models.CharField(max_length=50)
    back_forth = models.BooleanField(default=False)
    resarve_status = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    capicity = models.PositiveIntegerField()
    number_fly = models.PositiveIntegerField()
    situation = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    





