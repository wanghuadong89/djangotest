from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.Login,name='login'),
    url(r'^logout/$',views.Logout,name='logout'),

]
