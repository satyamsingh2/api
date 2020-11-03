from django.shortcuts import HttpResponse
from .models import Member
from django.views.generic import (ListView, DetailView)
#from django.core.paginator import Paginator

# Create your views here.
"""def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

"""


    
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
    template_name = 'detail.html'

    def get_object(self):
        id_ =self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)