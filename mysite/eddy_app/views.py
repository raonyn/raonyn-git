from multiprocessing import context
from django.shortcuts import render

##eddy_app
#from django.http import HttpResponse
from .models import Company

def index(request):
#    return HttpResponse("Hello. This is default Page.")
    company_list = Company.objects.all()
    context = {'company_list': company_list}
    
    return render(request, 'eddy_app/index.html', context)


# Create your views here.
