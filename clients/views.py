from django.shortcuts import render, get_object_or_404
from .models import Clients

def clients_list(request):
    clients = Clients.objects.all()
    return render(request, 'clients/clients_list.html', {'clients': clients})


def client_detail(request, pk):
    sel_client = Clients.objects.filter(client_id=pk)
    client = get_object_or_404(Clients, pk=sel_client)
    return render(request, 'clients/client_detail.html', {'client': client})
