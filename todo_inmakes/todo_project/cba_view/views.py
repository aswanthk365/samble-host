from django.shortcuts import render
from todo_app.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


class taksListView(ListView):
    model=task
    template_name='index.html'
    context_object_name='a'

class deatailView(DetailView):
    model=task
    template_name='deatail.html'
    context_object_name='a'

class updateview(UpdateView):

    model=task
    template_name='updated.html'
    fields=('task_name','priority','date')

    # success_url=reverse_lazy('listView')
    def get_success_url(self):
        return reverse_lazy('DeatailView', kwargs={'pk':self.object.id})
    
class cbvdelete(DeleteView):
    model=task
    template_name='deleteCbv.html'
    success_url=reverse_lazy('listView')