from django.shortcuts import HttpResponse
from users.models import Get
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def users(request):
    if request.method == "POST":
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        company_name = request.POST.get('company_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        email = request.POST.get('email')
        web = request.POST.get('web')
        age = request.POST.get('age')
        get = Get(id='id' , first_name ='first_name', last_name = 'last_name', company_name ='company_name',
        city = 'city', state = 'state', zip = 'zip', email = 'email', web = 'web', age = 'age')
        get.save()
       
