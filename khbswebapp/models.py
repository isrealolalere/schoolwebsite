from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Student_reg(models.Model):
    student_img = models.ImageField(upload_to='student-image/')
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = CountryField()
    student_address_city = models.CharField(max_length=250)
    student_address_state = models.CharField(max_length=100)
    student_address_country = CountryField()

class Parent_info(models.Model):
    student = models.ForeignKey(Student_reg, on_delete=models.CASCADE)
    father_img = models.ImageField(upload_to='parent-image/', null=True)
    mother_img = models.ImageField(upload_to='parent-image/', null=True)
    father_first_name = models.CharField(max_length=150)
    father_last_name = models.CharField(max_length=150)
    mother_first_name = models.CharField(max_length=150)
    mother_last_name = models.CharField(max_length=150)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=100, null=True)
    country          = CountryField()

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number1 = models.CharField(validators=[phone_regex], max_length=20)
    phone_number2 = models.CharField(validators=[phone_regex], max_length=20)
