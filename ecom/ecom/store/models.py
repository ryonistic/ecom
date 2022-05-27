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
    cost_price = models.PositiveBigIntegerField(default=99)
    stripe_product_id = models.CharField(max_length=100, null=True, blank=True)
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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)
    date_placed = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product)

class Review(models.Model):
    """
    Every review is connected to a product and has content filled 
    by the reviewer.
    """
    RATING_CHOICES = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    stars = models.CharField(max_length=3, choices=RATING_CHOICES, null=True)
    time_published = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.publisher)

    class Meta:
        ordering = ['-time_published']
