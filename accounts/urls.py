from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('home',views.index,name='Home'),
    path('table',views.ViewProduct,name='Table'),
    path('dashboard',views.dashboard,name='Dashboard'),
    path('post-data',views.postdata,name='post_data'),
    path('login',views.login,name='Login'),
    path('logout',views.logout,name='Logout'),
    path('createuser',views.CreateUser,name='CreateUser'),
    path('createproduct',views.CreateProduct,name='CreateProduct'),
    path('viewagencies',views.ViewAgencies,name='ViewAgencies'),
    path('viewproductforagency',views.ViewProductsforAgency,name='ViewProductforAgencies'),
    path('deleteuser',views.DeleteUser,name='DeleteUser'),
    path('addssl',views.AssignUsertoProduct,name='AssignUsertoProduct'),
    path('controlssl',views.ControlSSL,name='ControlSSL'),
    path('view',views.View,name='View'),
]