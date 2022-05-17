from django.conf import settings
from django.db import models
from PIL import Image



class Product(models.Model):
    TYPE_CHOICES = (
            ('Electronics', 'Electronics'),
            ('Cutlery', 'Cutlery'),
            ('Books', 'Books'),
            ('Clothing', 'Clothing'),
            ('Accessories', 'Accessories'),
            ('Others', 'Others'),
            )
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=99)
    date_added = models.DateField(auto_now_add=True)
    type = models.CharField(choices = TYPE_CHOICES, max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='products/', blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image.path)
            if image.height > 700 or image.width > 700:
                output_size = (700, 700)
                image.thumbnail(output_size)
                image.save(self.image.path)

    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return (f"{self.owner}'s cart")

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_placed = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
