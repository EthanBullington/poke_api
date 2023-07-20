from django.db import models
from django.utils import timezone

from django.core import validators as v
from .validators import validate_name
from django.core.exceptions import ValidationError

from move_app.models import Move

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, validators=[validate_name])
    level = models.PositiveIntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)]) #level cap at 100 and min of 1
    date_encountered = models.DateField(default="2008-01-01")
    date_captured = models.DateTimeField(default=timezone.now)
    description= models.TextField(default='Unknown', validators=[v.MinLengthValidator(25), v.MaxLengthValidator(150)])
    captured = models.BooleanField(default=False)

    #relations
    moves = models.ManyToManyField(Move, default=1)#create many to many relationship between pokemon and move
    
    def __str__(self):
        return self.name
    
    def level_up(self):
        self.level += 1
        self.save()

    def talk(self):
        return "Pokemon cries"
    
    def clean(self):
        if self.move.count() > 4:
            raise ValidationError("A Pokemon can have at most 4 moves.")