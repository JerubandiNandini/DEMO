from django.shortcuts import render
from .models import landscapes
from .models import Phones
from .models import Beaches
from .models import Houses

# Create your views here.
def index(request):
    category = landscapes.objects.all()
    category1 = Phones.objects.all()
    category2 = Beaches.objects.all()
    category3 = Houses.objects.all()
    return render(request, 'index.html', {'categories':category, 'categories':category1, 'categories':category2, 'categories':category3})