from django.db import models
from accounts.views import User
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    


