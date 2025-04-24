from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="uploads/",default="a.png")
    phone = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=20, unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    joined_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='contributions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=20, choices=[('cash', 'Cash'), ('mpesa', 'MPesa')])

    def __str__(self):
        return self.member

class SMSLog(models.Model):
    message = models.TextField()
    recipients = models.ManyToManyField(Member)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class MPesaPayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, default='pending')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
