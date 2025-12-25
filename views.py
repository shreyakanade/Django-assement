# views.py
from django.http import HttpResponse
from .models import MyModel

def test_view(request):
    print("Before save")
    MyModel.objects.create(name="Test")
    print("After save")
    return HttpResponse("Done")
