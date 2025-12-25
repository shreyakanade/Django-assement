# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal(sender, instance, **kwargs):
    print("Signal thread:", threading.get_ident())
