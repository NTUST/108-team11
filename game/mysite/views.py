from django.shortcuts import render,redirect,render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect

# login

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

#first and second grade for emico

def start(request):
	return render(request, '1-2/emico/1start.html')

def eatop(request):
	return render(request, '1-2/emico/2eatop.html')

def eatgood(request):
	return render(request, '1-2/emico/3-1eatgood.html')

def eatgood2(request):
	return render(request, '1-2/emico/3-2eatgood2.html')

def eatgood3(request):
	return render(request, '1-2/emico/3-3eatgood3.html')

def eatno(request):
	return render(request, '1-2/emico/3-4eatno.html')

def class1(request):
	return render(request, '1-2/emico/4class.html')

def classop(request):
	return render(request, '1-2/emico/5classop.html')

def classbook(request):
	return render(request, '1-2/emico/6-1classbook.html')

def classvideo(request):
	return render(request, '1-2/emico/6-2classvideo.html')

def classsleep(request):
	return render(request, '1-2/emico/6-3classsleep.html')

def home(request):
	return render(request, '1-2/emico/7home.html')

def homeop(request):
	return render(request, '1-2/emico/8homeop.html')

def homeop101(request):
	return render(request, '1-2/emico/9-1homeop1-1.html')

def eatgood4(request):
	return render(request, '1-2/emico/9-2-1eatgood4.html')

def eatgood5(request):
	return render(request, '1-2/emico/9-2-2eatgood5.html')

def eatgood6(request):
	return render(request, '1-2/emico/9-2-3eatgood6.html')

def eatgood7(request):
	return render(request, '1-2/emico/9-2-4eatgood7.html')

def eatop2(request):
	return render(request, '1-2/emico/9-2eatop2.html')

def homeop103(request):
	return render(request, '1-2/emico/9-3homeop1-3.html')

def homeop104(request):
	return render(request, '1-2/emico/9-4homeop1-4.html')

def club(request):
	return render(request, '1-2/emico/10club.html')

def club1(request):
	return render(request, '1-2/emico/11-1club1.html')

def club2(request):
	return render(request, '1-2/emico/11-2club2.html')

def club3(request):
	return render(request, '1-2/emico/11-3club3.html')

def lover(request):
	return render(request, '1-2/emico/12lover.html')

def loverop(request):
	return render(request, '1-2/emico/13loverop.html')

def loverlove(request):
	return render(request, '1-2/emico/14-1-1loverlove.html')

def loverlove2(request):
	return render(request, '1-2/emico/14-1-2loverlove2.html')

def loverlove3(request):
	return render(request, '1-2/emico/14-1-3loverlove3.html')

def lovertalk(request):
	return render(request, '1-2/emico/14-2lovertalk.html')

def camp(request):
	return render(request, '1-2/emico/15camp.html')

def campgo(request):
	return render(request, '1-2/emico/16campgo.html')

def midterm(request):
	return render(request, '1-2/emico/17midterm.html')

def midtermop(request):
	return render(request, '1-2/emico/18midtermop.html')

def prom(request):
	return render(request, '1-2/emico/19prom.html')

def promgo(request):
	return render(request, '1-2/emico/20promgo.html')

def final(request):
	return render(request, '1-2/emico/21final.html')

def winterVacation1(request):
	return render(request, '1-2/emico/22winterVacation1.html')

def winterVacation101(request):
	return render(request, '1-2/emico/23-1winterVacation1-1.html')

def winterVacation102(request):
	return render(request, '1-2/emico/23-2winterVacation1-2.html')

def winterVacationEnd1(request):
	return render(request, '1-2/emico/24winterVacationEnd1.html')

def ktv(request):
	return render(request, '1-2/emico/25ktv.html')

def ktvgo(request):
	return render(request, '1-2/emico/26ktvgo.html')

def secondDrop1(request):
	return render(request, '1-2/emico/27secondDrop1.html')

def secondDrop1ok(request):
	return render(request, '1-2/emico/28secondDrop1ok.html')

def summerVacation1(request):
	return render(request, '1-2/emico/29summerVacation1.html')

def summerVacation101(request):
	return render(request, '1-2/emico/30-1summerVacation1-1.html')

def summerVacation102(request):
	return render(request, '1-2/emico/30-2summerVacation1-2.html')

def summerVacation103(request):
	return render(request, '1-2/emico/30-3summerVacation1-3.html')

def summerVacation104(request):
	return render(request, '1-2/emico/30-4summerVacation1-4.html')

def rentHouse(request):
	return render(request, '1-2/emico/31rentHouse.html')

def sophomoreOp(request):
	return render(request, '1-2/emico/32sophomoreOp.html')

def sophomoreOp101(request):
	return render(request, '1-2/emico/33-1sophomoreOp1-1.html')

def sophomoreOp102(request):
	return render(request, '1-2/emico/33-2sophomoreOp1-2.html')

def sophomoreOp103(request):
	return render(request, '1-2/emico/33-3sophomoreOp1-3.html')

def sophomoreOp104(request):
	return render(request, '1-2/emico/33-4sophomoreOp1-4.html')

def lover2(request):
	return render(request, '1-2/emico/34lover2.html')

def loverop2(request):
	return render(request, '1-2/emico/35loverop2.html')

def loverok(request):
	return render(request, '1-2/emico/36-1loverok.html')

def loverEnd(request):
	return render(request, '1-2/emico/36-2loverEnd.html')

def secondDrop2(request):
	return render(request, '1-2/emico/37secondDrop2.html')

def secondDrop2ok(request):
	return render(request, '1-2/emico/38secondDrop2ok.html')

def winterVacation2(request):
	return render(request, '1-2/emico/39winterVacation2.html')

def winterVacation201(request):
	return render(request, '1-2/emico/40-1winterVacation2-1.html')

def winterVacation202(request):
	return render(request, '1-2/emico/40-2winterVacation2-2.html')

def sophomore2(request):
	return render(request, '1-2/emico/41sophomore2.html')

def finalExam2(request):
	return render(request, '1-2/emico/42finalExam2.html')

def summerVacation2(request):
	return render(request, '1-2/emico/43summerVacation2.html')

def summerVacation201(request):
	return render(request, '1-2/emico/44-1summerVacation2-1.html')

def summerVacation202(request):
	return render(request, '1-2/emico/44-2summerVacation2-2.html')

def summerVacation203(request):
	return render(request, '1-2/emico/44-3summerVacation2-3.html')

def summerVacation204(request):
	return render(request, '1-2/emico/44-4summerVacation2-4.html')

#first and second grade for karen