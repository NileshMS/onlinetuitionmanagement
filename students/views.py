from django.shortcuts import render
from django.views.generic import ListView,DetailView
from tutionadmin.models import AddCourse
# Create your views here.
class CourseListViews(ListView):
    model = AddCourse
    template_name = 'home.html'

class CourseDetailViews(DetailView):
    model = AddCourse
    template_name = 'course_detail_view.html'


