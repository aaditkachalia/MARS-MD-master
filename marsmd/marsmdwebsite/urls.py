from django.urls import path
from django.conf.urls import include, url 
from . import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
    url(r'^home/', views.index, name='index'),
    url(r'^admin_index/', views.sbadminIndex, name='index'),
    url(r'^admin_Login/', views.adminLogin, name='index'),
    url(r'^tables/', views.tables, name='index'),
    url(r'^charts/', views.charts, name='index'),
    url(r'^register/', views.register, name='index'),
    url(r'^activity/', views.activity, name='index'),
    url(r'^familyadded/', views.familyadded, name='index'),
    url(r'^history/', views.history, name='index'),
    url(r'^hearts/', views.hearts, name='index'),
    url(r'^nutrition/', views.nutrition, name='index'),


    ]