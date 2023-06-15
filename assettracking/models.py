from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    serial_number = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Checkout(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.device} - {self.employee}"

class ConditionLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_condition = models.CharField(max_length=100)
    checked_in_condition = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.device} - {self.date}"
