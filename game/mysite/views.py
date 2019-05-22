from django.shortcuts import render,redirect,render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homePage(request):
	template = get_template('startGame.html')
	html = template.render(locals())
	return HttpResponse(html)

def startGame(request):
	return HttpResponseRedirect('/')

def selectCharactor(request):
	return render(request, 'selectCharactor.html')

def gameIntroduction(request):
	return render(request, 'gameIntroduction.html')

def teamIntroduction(request):
	return render(request, 'teamIntroduction.html')

def settings1(request):
	return render(request, 'settings1.html')

def settings2(request):
	return render(request, 'settings2.html')


def settings3(request):
	return render(request, 'settings3.html')


def settings4(request):
	return render(request, 'settings4.html')
