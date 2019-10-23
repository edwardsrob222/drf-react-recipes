from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Recipe(models.Model):
    OVEN = 'OVEN'
    STOVE = 'STOVE'
    MICROWAVE = 'MICROWAVE'


    COOKING_METHODS = [
    (OVEN, 'Oven'),
    (STOVE, 'Stove'),
    (MICROWAVE, 'Microwave'),
    ]


    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cook_method = models.CharField(max_length=255, choices=COOKING_METHODS, default=MICROWAVE)
    cook_time = models.CharField(max_length=255, default=1)
    prep_time = models.CharField(max_length=255, default=1)
    cook_temp = models.CharField(max_length=255, default=1)
    ingredients = models.CharField(max_length=255, default=1)


    def __str__(self):
        return self.title
