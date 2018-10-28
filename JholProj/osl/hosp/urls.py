from django.urls import path
from . import views
from django.conf.urls import include, url 

app_name = 'hosp'

urlpatterns = [
    # /hosp/
    url(r'^$', views.doctors, name='login'),

    path('hosp/', views.IndexView.as_view(), name='index'),
    # /hosp/id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /hosp/patient/add/
    path('patient/add/', views.PatientCreate.as_view(), name='patient-add'),
    # /hosp/patient/id/
    path('patient/<int:pk>/', views.PatientUpdate.as_view(), name='patient-update'),
    # /hosp/patient/id/delete/
    path('patient/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient-delete'),
    # /hosp/signup/
    path('signup/', views.UserFormView.as_view(), name='register'),
    #/hosp/login/
    path('login/', views.login_user, name='login'),
    #/hosp/logout/
    path('logout/', views.logout_user, name='logout'),
    #/hosp/doctor/
    path('doctors/', views.doctors, name='doctors'),

]
