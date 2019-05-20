from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

def homePage(request):
	template = get_template('startGame.html')
	html = template.render(locals())
	return HttpResponse(html)
	