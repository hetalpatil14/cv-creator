from django.urls import path 
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.data, name='data'),
    path('person/<int:pk>/',views.edit,name = 'edit'),
    path('person/new/', views.create, name= 'create'),
    # path('viewdata/', views.viewdata, name = 'viewdata'),
    # path('editdata/<int:pk>', views.editdata, name = 'editdata'),
    path('person/<int:pk>/edit/', views.update, name = 'update'),
    path('person/<int:pk>/viewdata/', views.viewdata, name = 'viewdata'),
    path('person/<int:pk>/register/', views.register, name = 'register'),
    path('person/<int:pk>/delete', views.delete, name ='delete'),
    # path('person/<int:pk>/delete', views.delete, name ='delete'),
]
