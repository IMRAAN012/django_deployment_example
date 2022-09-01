from django.shortcuts import render

# Create your views here.
def basic(request):


    return render(request,'basic_App/base.html')

def index(request):
    return render(request,'basic_App/index.html')

def other(request):
    my_dict = {'sentence':['hello','naveeth','shiek','imraan!'],'age':25,}
    return render(request,'basic_App/other.html',context=my_dict)

def relative(request):
    return render(request,'basic_App/relative_url.html')
