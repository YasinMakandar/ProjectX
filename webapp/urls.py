from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name=""),

  path('register', views.register, name="register"),

  path('login', views.my_login, name="my_login"),

  path('dashboard', views.dashboard, name='dashboard'),

  path('user_logout', views.user_logout, name="user_logout"),

  path('create_record', views.create_record, name="create_record"),

  path('update_record/<int:pk>', views.update_record, name='update_record'),

  path('record/<int:pk>', views.singular_record, name="record"),

  path('delete_record/<int:pk>', views.delete_record, name="delete_record")
]
