from django.shortcuts import render
from .models import Clients

def clients_list(request):
    clients = Clients.objects.all()
    return render(request, 'clients/clients_list.html', {'clients': clients})
