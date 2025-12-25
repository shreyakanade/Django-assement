# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, LogModel

@receiver(post_save, sender=MyModel)
def my_signal(sender, instance, **kwargs):
    LogModel.objects.create(message="Signal executed")
