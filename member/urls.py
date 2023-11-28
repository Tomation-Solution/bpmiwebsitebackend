from django.urls import path
from . import views


urlpatterns =[
path('',views.register_become_a_member,name='register_become_a_member')
]