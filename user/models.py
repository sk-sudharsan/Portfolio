from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

from django.db import models

class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    description = models.TextField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    place = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/', null=True, blank=True)  # ImageField for personal image
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Education(models.Model):
    portfolio = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    graduation_year = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.course)

class Experience(models.Model):
    portfolio = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return '{}'.format(self.title)

class Project(models.Model):
    portfolio = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=200, default='website')
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)  # ImageField for project image
    def __str__(self):
        return '{}'.format(self.title)

class Skills(models.Model):
    portfolio = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return '{}'.format(self.skill)

class resume(models.Model):
    portfolio = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cv = models.ImageField(upload_to='resumes/')

    def __str__(self):
        return '{}'.format(self.title)

