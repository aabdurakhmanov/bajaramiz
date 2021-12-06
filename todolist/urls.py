from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='logout'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('update_task/', TaskCreate, name='update_task'),
    path('update_task/<str:pk>/', TaskCreate, name="update_task"),
    path('delete/<str:pk>/', deleteTask, name="delete"),

]