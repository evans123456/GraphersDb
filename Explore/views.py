from django.views import generic
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from.models import Pictures


class IndexView(generic.ListView):
	template_name = "explore/index.html"
	context_object_name = "all_pictures"

	def get_queryset(self):
		return Pictures.objects.all()

class DetailView(generic.DetailView):
	model = Pictures
	context_object_name = "pic"
	template_name = "explore/details.html"


class AddImage(CreateView):#Album create
	model = Pictures#album
	fields = ['category','post','post_title']
	template_name = "explore/addimage_form.html"



#after creating the classview create the template 

#in the template  href="{% url 'explore:image-add' %}">(the href was based on the name you gave it in the urls.py)
#you also need to add the context_object_name to access the variable name in the jinja area