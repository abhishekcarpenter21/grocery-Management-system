from django.urls import path
from .import views

urlpatterns=[
    path('',views.user_login,name='login'),
    path('products',views.index, name='Home'),
    path('add/',views.add_product,name='add_product'),
    path('del/<int:id>/',views.del_product,name='del'),
    path('update/<int:id>/',views.update_product,name='update'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.user_register, name='register')
]