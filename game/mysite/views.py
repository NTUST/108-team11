from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

def homePage(request):
	template = get_template('startGame.html')
	html = template.render(locals())
	return HttpResponse(html)

def selectCharactor(request):
	template = get_template('selectCharactor.html')
	html = template.render(locals())
	return HttpResponse(html)

def gameIntroduction(request):
	template = get_template('gameIntroduction.html')
	html = template.render(locals())
	return HttpResponse(html)

def teamIntroduction(request):
	template = get_template('teamIntroduction.html')
	html = template.render(locals())
	return HttpResponse(html)

def settings1(request):
	template = get_template('settings1.html')
	html = template.render(locals())
	return HttpResponse(html)

def settings2(request):
	template = get_template('settings2.html')
	html = template.render(locals())
	return HttpResponse(html)

def settings3(request):
	template = get_template('settings3.html')
	html = template.render(locals())
	return HttpResponse(html)

def settings4(request):
	template = get_template('settings4.html')
	html = template.render(locals())
	return HttpResponse(html)