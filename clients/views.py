from django.shortcuts import render

def clients_list(request):
    return render(request, 'clients/clients_list.html', {})
