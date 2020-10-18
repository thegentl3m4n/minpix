from django.shortcuts import render
from .models import IMage
from django.views.generic import ListView, CreateView

# Create your views here.


def home(request):
	return render(request, 'main/home.html')



class ImageListView(ListView):
	model = IMage
	template_name = 'main/image_list.html'
	context_object_name = 'IMage'
	ordering = ['-date_added']
	
class ImageCreateView(CreateView):
	model = IMage
	fields = ['title', 'image_file']
	
