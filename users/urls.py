from django.urls import path

from . import views
from .views import MemberDetail, MemberList, MemberCreate, MemberUpdate, MemberDelete

app_name='users'
urlpatterns = [
    #path('', views.index, name='index'),
    
    path('users/<int:pk>/', MemberDetail.as_view(), name='detail'),
    path('users/', MemberList.as_view(),name='users'),
    path('users/update/<int:pk>/', MemberUpdate.as_view(), name='update'),
    path('users/create/', MemberCreate.as_view(), name='member-create'),
    path('users/delete/<int:pk>/', MemberDelete.as_view(), name='delete'),
]