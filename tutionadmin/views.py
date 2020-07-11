from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import AddCourseForm, MainAdminRegisterForm, AdminLoginForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import MainAdminRegister, AddCourse
from django.views.generic import UpdateView, DeleteView


# @login_required(login_url='/tutionadmin:login/')
def addcourse(request):
    form = AddCourseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tutionadmin:adminhome')
        else:
            redirect('tutionadmin:addcourse')
    else:
        form = AddCourseForm()
    return render(request, 'tutionadmin/registercourse.html', {'form': form})


def login(request):
    form = AdminLoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username').title()
        password = request.POST.get('password')
        adminname = get_object_or_404(MainAdminRegister, username=username)
        if adminname:
            flag = check_password(password, adminname.password)
            if flag:
                # request.session['member_id'] = adminname.id
                return redirect('tutionadmin:adminhome')
            else:
                raise ValidationError('Enter correct Password')
        else:
            raise ValidationError('enter correct username.')
    else:
        return render(request, 'tutionadmin/adminlogin.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = MainAdminRegisterForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password')
            password1 = make_password(password)
            username = request.POST.get('username')
            MainAdminRegister(username=username,
                              password=password1).save()
            return HttpResponse('Welcome Admin')
        else:
            return HttpResponse(form.errors)
    else:
        form = MainAdminRegisterForm()
        return render(request, 'tutionadmin/adminregister.html', {'form': form})


# @login_required(login_url='tutionadmin:login')
def Adminhome(request):
    courses = AddCourse.objects.all()

    # list of registered courses
    # update course info and delete course info
    return render(request, 'tutionadmin/admin_home.html', {'courses': courses})


# def update(request):
#     queryset = AddCourse.objects.filter(id=id)
#     print(queryset)
#     form = AddCourseForm()
#     return render(request, 'tutionadmin/update.html', {'course': form})

class Update(UpdateView):
    model = AddCourse
    template_name = 'tutionadmin/update.html'
    form_class = AddCourseForm
    success_url = reverse_lazy('tutionadmin:adminhome')
#  It is useful for when you need to use a URL reversal before your project’s URLConf is loaded.
# Some common cases where this function is necessary are:
# providing a reversed URL as the url attribute of a generic class-based view
class Delete(DeleteView):
    model = AddCourse
    template_name = 'tutionadmin/delete.html'
    success_url = reverse_lazy('tutionadmin:adminhome')


def logout(request):
    return redirect('tutionadmin:login')
