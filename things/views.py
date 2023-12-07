from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from things.forms import ThingForm

@csrf_protect
def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
