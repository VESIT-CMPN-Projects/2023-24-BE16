from django.db import models
from PIL import Image

from account.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_barter = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE,default=10)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Resize the image if needed
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class BarterRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='barter_requests_sent')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15,default=9325462397)
    address = models.CharField(max_length=255, default="Unknown Address")


class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_transactions')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_barter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
