from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    is_special = models.BooleanField(default=False)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)

    def __str__(self):
        return self.name