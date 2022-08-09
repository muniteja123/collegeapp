from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    marks = models.IntegerField()
    intermediate = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Register(models.Model):
    apply = models.OneToOneField(Apply, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.ImageField()
    fname = models.CharField(max_length=300)
    nationality = models.CharField(max_length=300)

    def __str__(self):
        return self.password

class Department(models.Model):
    register = models.ManyToManyField(Register, blank=True)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department

