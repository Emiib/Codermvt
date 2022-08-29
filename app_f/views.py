from django.shortcuts import render
from .models import family


def inicio(request):

    my_family = family.objects.all()
    
    return render(request, 'index.html', {'my_family':my_family})




