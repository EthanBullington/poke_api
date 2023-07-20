from django.db import models
from django.core import validators as v

from django.core.exceptions import ValidationError
from .validators import validate_move_name
# Create your models here.

class Move(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, validators=[validate_move_name])
    accuracy = models.PositiveIntegerField(default=70, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    maxPP = models.IntegerField(default=20, validators=[v.MinValueValidator(5), v.MaxValueValidator(30)])
    pp = models.IntegerField(default=20 , validators=[v.MinValueValidator(1)])
    power = models.PositiveIntegerField(default=80, validators=[v.MaxValueValidator(120)])


    def __str__(self):
        return f"{self.name} | accuracy: {self.accuracy} | power: {self.power} | current_pp: {self.pp}/{self.maxPP} |"
    
    def increase_max_pp(self, increment):
        self.maxPP += increment
        self.save()

    def clean(self):
        if self.pp > self.maxPP:
            raise ValidationError("PP can't be higher than Max PP")
        