from django.http import HttpResponse
from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    context = {
        'name': 'Marcelo'
    }
    return render(request, 'app/index.html', context)

def users(request):
    email = request.POST['email']
    Member.objects.create(email=email)
    members = Member.objects.all()
    context = {
        'email': email,
        'members': members,
    }
    return render(request, 'app/members.html', context)

def users_name(request, name):
    return HttpResponse(f"Hola {name}")