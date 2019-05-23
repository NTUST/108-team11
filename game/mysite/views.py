from django.shortcuts import render,redirect,render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homePage(request):
	template = get_template('login/startGame.html')
	html = template.render(locals())
	return HttpResponse(html)

def startGame(request):
	return HttpResponseRedirect('/')

def selectCharactor(request):
	return render(request, 'login/selectCharactor.html')

def gameIntroduction(request):
	return render(request, 'login/gameIntroduction.html')

def teamIntroduction(request):
	return render(request, 'login/teamIntroduction.html')

def settings1(request):
	template = get_template('login/settings1.html')
	html = template.render(locals())
	return HttpResponse(html)


def settings2(request):
	return render(request, 'login/settings2.html')


def settings3(request):
	return render(request, 'login/settings3.html')


def settings4(request):
	return render(request, 'login/settings4.html')
