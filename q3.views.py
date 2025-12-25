# views.py
from django.db import transaction
from django.http import HttpResponse
from .models import MyModel

def test_view(request):
    try:
        with transaction.atomic():
            MyModel.objects.create(name="Transaction Test")
            raise Exception("Force rollback")
    except Exception:
        pass

    return HttpResponse("Done")
