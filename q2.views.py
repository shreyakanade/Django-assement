# views.py
import threading
from django.http import HttpResponse
from .models import MyModel

def test_view(request):
    print("View thread:", threading.get_ident())
    MyModel.objects.create(name="Thread Test")
    return HttpResponse("Done")
