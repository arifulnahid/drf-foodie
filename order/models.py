from django.db import models
from django.contrib.auth.models import User
from item.models import Item


STATUS = (
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
    ('Delivered', 'Delivered'),
)

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    payment = models.BooleanField(default=False)
    status = models.CharField(max_length=45, choices=STATUS, default='Pending')
    total_price = models.IntegerField()