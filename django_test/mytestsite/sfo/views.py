from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import SFO

# Create your views here.
def index(request):
    mysfo = SFO.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mysfo': mysfo
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['name']
  y = request.POST['modul']
  z = request.POST['gruppe']
  sfo = SFO(name=x, modul=y, gruppe=z)
  sfo.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  sfo = SFO.objects.get(id=id)
  sfo.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mysfo = SFO.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mysfo': mysfo,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  modul = request.POST['modul']
  gruppe = request.POST['gruppe']
  mandag = request.POST['mandag']
  tirsdag = request.POST['tirsdag']
  onsdag = request.POST['onsdag']
  torsdag = request.POST['torsdag']
  fredag = request.POST['fredag']
  sfo = SFO.objects.get(id=id)
  sfo.name = name
  sfo.modul = modul
  sfo.gruppe = gruppe
  sfo.mandag = mandag
  sfo.tirsdag = tirsdag
  sfo.onsdag = onsdag
  sfo.torsdag = torsdag
  sfo.fredag =fredag
  sfo.save()
  return HttpResponseRedirect(reverse('index'))
