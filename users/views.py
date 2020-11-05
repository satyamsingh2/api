from django.shortcuts import HttpResponse
from .models import Member
from django.views.generic import (CreateView, ListView, DetailView, UpdateView, DeleteView)
from .forms import MemberModelForm, MemModelForm
#from django.core.paginator import Paginator

# Create your views here.



class MemberCreate(CreateView):
    template_name='users/create.html'
    queryset=Member.objects.all()
    form_class = MemberModelForm
    success_url='/api/users/'
       
class MemberList(ListView):
    model = Member
    
    
    """member = Member.objects.all()
    member_paginator = Paginator(member, 10)
    page = member_paginator.get_page(1)
    context = {
        'count' : member_paginator.count,
        'page' : page
    }"""

class MemberDetail(DetailView):
    model = Member
    template_name = 'users/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class MemberUpdate(UpdateView):
    
    template_name='users/create.html'
    queryset=Member.objects.all()
    form_class = MemModelForm
    success_url='/api/users/' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MemberDelete(DeleteView):
    model=Member
    template_name = 'users/delete.html'
    context_object_name='first_name'
    success_url='/api/users/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
