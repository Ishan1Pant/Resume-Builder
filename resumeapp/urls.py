from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('<int:id>/',views.profile,name='profile'),
    path('all/',views.list_item,name='list'),

]