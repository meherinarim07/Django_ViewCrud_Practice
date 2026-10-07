from django.shortcuts import render,redirect
from .models import laptop
from .forms import LaptopForm
# Create your views here.
def laptop_view(request):
    p=laptop.objects.all()
    return render(request,'laptop-view.html',{"p":p})

def add(request):
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laptop_view')
    else:
        form=LaptopForm()
    return render(request,'add.html',{'form':form})

def update(request,pk):
    p=laptop.objects.get(pk=pk)
    if request.method=='POST':
        form=LaptopForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return redirect('laptop_view')
    else:
        form=LaptopForm(instance=p)
    return render(request,'add.html',{'form':form})

def delete(request,pk):
    laptop.objects.get(pk=pk).delete()
    return redirect('laptop_view')

def details(request,pk):
    l=laptop.objects.get(pk=pk)
    return render(request,'details.html',{"l":l})