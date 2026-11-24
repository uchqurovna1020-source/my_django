from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def salom_ber(request):
    return HttpResponse("hello world")




def oquvchi_royxati(request):
    context = {}
    return render(request, 'hechnarsa.html', context)



def personal(request):
  context = {}
  return render(request, 'personal.html', context)


def personal2(request):
  context = {}
  return render(request, 'personal2.html', context)


def personal3(request):
  context = {}
  return render(request, 'personal3.html', context)


def personal4(request):
  context = {}
  return render(request, 'personal4.html', context)


def personal5(request):
  context = {}
  return render(request, 'personal5.html', context)