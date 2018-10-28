
from django.views import generic
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'hosp/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return Patient.objects.filter(doctor__contains=self.request.user).order_by('patient_firstname')


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Patient
    template_name = 'hosp/detail.html'


@method_decorator(login_required, name='dispatch')
class PatientCreate(CreateView):
    model = Patient
    fields = ['patient_firstname','patient_surname','disease_type','patient_photo','affected_region_photo','doctor','terminal']


@method_decorator(login_required, name='dispatch')
class PatientUpdate(UpdateView):
    model = Patient
    fields = ['patient_firstname', 'patient_surname', 'disease_type', 'patient_photo','terminal', 'doctor','affected_region_photo']


@method_decorator(login_required, name='dispatch')
class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('hosp:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'hosp/registeration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('hosp:index')
        return render(request, self.template_name, {'form':form})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'hosp/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('hosp:index')
            else:
                return render(request, 'hosp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'hosp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'hosp/login.html')


def doctors(request):
    users = User.objects.all()
    return render(request,'hosp/doctors.html',{'users':users})
