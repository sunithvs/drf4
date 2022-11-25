from datetime import timezone

from django.db import models

# Create your models here.
"""
This model for creating a coupon
"""


class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.code

    """
    function to check if the coupon is valid or not
    """

    def is_valid(self):
        return self.active and self.valid_from <= timezone.now() <= self.valid_to


"""
A model to create a session 
"""


# model for instructor
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.ImageField(upload_to='profile', blank=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    coupon = models.ManyToManyField(Coupon, related_name='sessions', blank=True)
    instructors = models.ManyToManyField(Instructor, related_name='sessions', blank=True)

    def __str__(self):
        return self.name

    """ function to check if the session is active or not"""

    def is_active(self):
        return self.start_date <= timezone.now() <= self.end_date
