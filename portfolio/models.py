from django.db import models
from datetime import date

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    details = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    details = models.TextField(max_length=500)
    start_date = models.DateField(default=date.today())
    finish_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title


class Education(models.Model):
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    gpa = models.FloatField(max_length=5)
    start_date = models.DateField(default=date.today())
    finish_date = models.DateField(default=date.today)


class Interest(models.Model):
    about = models.TextField(max_length=5000)


class Skill(models.Model):

    title_choice = [
        ('LANGUAGE', 'La'),
        ('FRAMEWORK', 'Fr'),
        ('VERSION CONTROL', 'Vc')
    ]
    title = models.CharField(max_length=15, choices=title_choice,
                             default='LANGUAGE')
    name = models.CharField(max_length=50)
    print(title)
