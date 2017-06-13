from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from color_liker.models import Color

# Create your views here.
MIN_SEARCH_CHARS = 2

class ColorList(ListView):
	model = Color
	context_object_name = 'colors'

	def dispatch(self, request, *args, **kwargs):
		self.request = request
		return super(ColorList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		return super(ColorList, self).get_queryset()

	def get_context_data(self, **kwargs):
		context = super(ColorList, self).get_context_data(**kwargs)

		global MIN_SEARCH_CHARS
		search_text = ""
		if(self.request.method =="GET"):
			search_text = self.request.GET.get("search_text", "").strip()
			if(len(search_text) < MIN_SEARCH_CHARS):
				search_text = ""

		if(search_text != ""):
			color_search_results = Color.objects.filter(name__contains=search_text)
		else:
			color_search_results = []

		context["search_text"] = search_text
		context["color_search_results"] = color_search_results

		context['MIN_SEARCH_CHARS'] = MIN_SEARCH_CHARS
		return context

def toggle_color_like(request, color_id):
	color = None
	try:
		color = Color.objects.filter(id=color_id)[0]
	except Color.DoesNotExist as e:
		raise ValueError("Unknown color.id=" + str(color_id) + ".original error:" + str(e))

	color.is_favorited = not color.is_favorited
	color.save()

	return render_to_response("color_liker/color_like_link__html_snippet.txt", {"color": color})

def submit_color_search_from_ajax(request):
	colors = []
	global MIN_SEARCH_CHARS

	search_text = ""
	if(len(request.method == 'GET')):
		search_text = request.GET.get('color_search_text', "").strip().lower()
		if(len(search_text) < MIN_SEARCH_CHARS):
			search_text = ""

	color_results = []
	if(search_text !=""):
		color_results = Color.objects.filter(name__contains=search_text)

	context = {
		"search_text": search_text,
		"color_search_results": color_results,
		"MIN_SEARCH_CHARS": MIN_SEARCH_CHARS,
	};
	return render_to_response('color_liker/color_search_results__html_snippet.txt', context)

