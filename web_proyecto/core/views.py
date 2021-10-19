from django.views.generic.list import ListView
from .models import Portada

class inicio(ListView):
    model = Portada

