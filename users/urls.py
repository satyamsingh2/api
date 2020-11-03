from django.urls import path

from . import views
from .views import MemberDetail, MemberList, MemberCreate, MemberUpdate, MemberDelete

app_name='users'
urlpatterns = [
    #path('', views.index, name='index'),
    
    path('detail/<int:pk>/', MemberDetail.as_view(), name='detail'),
    path('member_list/', MemberList.as_view()),
    path('update/<int:pk>/', MemberUpdate.as_view(), name='update'),
    path('create/', MemberCreate.as_view(), name='member-create'),
    path('delete/<int:pk>/', MemberDelete.as_view(), name='delete'),
]