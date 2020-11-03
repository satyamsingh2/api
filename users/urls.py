from django.urls import path

from . import views
from .views import MemberDetail, MemberList, MemberCreate, MemberUpdate, MemberDelete

app_name='users'
urlpatterns = [
    #path('', views.index, name='index'),
    
    path('users/<int:pk>-GET/', MemberDetail.as_view(), name='detail'),
    path('users-POST/', MemberList.as_view()),
    path('users/<int:pk>-PUT/', MemberUpdate.as_view(), name='update'),
    path('users/create/', MemberCreate.as_view(), name='member-create'),
    path('users/<int:pk>-DELETE/', MemberDelete.as_view(), name='delete'),
]