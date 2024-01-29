from django.shortcuts import render,redirect
from . models import *
from . forms import *
# Create your views here.

def index(request):
    if request.method=='POST':
        task_name=request.POST.get('task_name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task_obj=task(task_name=task_name,priority=priority,date=date)
        task_obj.save()
    a=task.objects.all()
    return render(request,'index.html',{'a':a})

def delete(request,id):
    get_id=task.objects.get(id=id)
    if request.method=='POST':
        get_id.delete()
        return redirect('/')
    return render(request,'delete.html',{'id':get_id})

def update(request,id):
    task_id=task.objects.get(id=id)
    form=update_form(request.POST or None,instance=task_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})


        



