from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse(
        "helloworld"
    );

def printMyName(request):
    return HttpResponse(
        "Sheraz"
    );


def printDynamic(request):
    myname="Sheraz"
    mygpa=3.0
    return render(request, 'dynamicPage.html', {'name':myname,'gpa':mygpa})

