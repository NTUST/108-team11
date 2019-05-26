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

#emico 1-2

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

#emico 3-4

def rdGrade(request):
	return render(request, '3-4/emico/45_3rdGrade.html')

def rdGradeOp(request):
	return render(request, '3-4/emico/46_3rdGradeOp.html')

def exchangeOp(request):
	return render(request, '3-4/emico/47_exchangeOp.html')

def countriesOp(request):
	return render(request, '3-4/emico/47-1_countriesOp.html')

def USA(request):
	return render(request, '3-4/emico/47-1-1_USA.html')

def Australia(request):
	return render(request, '3-4/emico/47-1-2_Australia.html')

def Germany(request):
	return render(request, '3-4/emico/47-1-3_Germany.html')

def France(request):
	return render(request, '3-4/emico/47-1-4_France.html')

def exchangeN(request):
	return render(request, '3-4/emico/47-2_exchangeN.html')

def exchangeY(request):
	return render(request, '3-4/emico/48_exchangeY.html')

def volleyballCaptonOp(request):
	return render(request, '3-4/emico/49_volleyballCaptonOp.html')

def captonY(request):
	return render(request, '3-4/emico/49-1_captonY.html')

def captonN(request):
	return render(request, '3-4/emico/49-2_captonN.html')

def summerVacation3Op(request):
	return render(request, '3-4/emico/50_summerVacation3Op.html')

def summerVacation31(request):
	return render(request, '3-4/emico/50-1_summerVacation3.html')

def summerVacation32(request):
	return render(request, '3-4/emico/50-2_summerVacation3.html')

def summerVacation33(request):
	return render(request, '3-4/emico/50-3_summerVacation3.html')

def summerVacation34(request):
	return render(request, '3-4/emico/50-4_summerVacation3.html')

def senior(request):
	return render(request, '3-4/emico/51_senior.html')

def seniorOp(request):
	return render(request, '3-4/emico/52_seniorOp.html')

def internshipOp(request):
	return render(request, '3-4/emico/52-1_internshipOp.html')

def masterOp(request):
	return render(request, '3-4/emico/52-2_masterOp.html')

def takeExam(request):
	return render(request, '3-4/emico/53_takeExam.html')

def work(request):
	return render(request, '3-4/emico/53_work.html')

def finalExamOp(request):
	return render(request, '3-4/emico/54_finalExamOp.html')

def graduation(request):
	return render(request, '3-4/emico/55_graduation.html')

def finishGame(request):
	return render(request, '3-4/emico/56_finishGame.html')

def gameOver(request):
	return render(request, 'end/gameOver.html')








#karen 1-2 grade

def startk(request):
	return render(request, '1-2/karen/1start.html')

def eatopk(request):
	return render(request, '1-2/karen/2eatop.html')

def eatgoodk(request):
	return render(request, '1-2/karen/3-1eatgood.html')

def eatgood2k(request):
	return render(request, '1-2/karen/3-2eatgood2.html')

def eatgood3k(request):
	return render(request, '1-2/karen/3-3eatgood3.html')

def eatnok(request):
	return render(request, '1-2/karen/3-4eatno.html')

def class1k(request):
	return render(request, '1-2/karen/4class.html')

def classopk(request):
	return render(request, '1-2/karen/5classop.html')

def classbookk(request):
	return render(request, '1-2/karen/6-1classbook.html')

def classvideok(request):
	return render(request, '1-2/karen/6-2classvideo.html')

def classsleepk(request):
	return render(request, '1-2/karen/6-3classsleep.html')

def homek(request):
	return render(request, '1-2/karen/7home.html')

def homeopk(request):
	return render(request, '1-2/karen/8homeop.html')

def homeop101k(request):
	return render(request, '1-2/karen/9-1homeop1-1.html')

def eatgood4k(request):
	return render(request, '1-2/karen/9-2-1eatgood4.html')

def eatgood5k(request):
	return render(request, '1-2/karen/9-2-2eatgood5.html')

def eatgood6k(request):
	return render(request, '1-2/karen/9-2-3eatgood6.html')

def eatgood7k(request):
	return render(request, '1-2/karen/9-2-4eatgood7.html')

def eatop2k(request):
	return render(request, '1-2/karen/9-2eatop2.html')

def homeop103k(request):
	return render(request, '1-2/karen/9-3homeop1-3.html')

def homeop104k(request):
	return render(request, '1-2/karen/9-4homeop1-4.html')

def clubk(request):
	return render(request, '1-2/karen/10club.html')

def club1k(request):
	return render(request, '1-2/karen/11-1club1.html')

def club2k(request):
	return render(request, '1-2/karen/11-2club2.html')

def club3k(request):
	return render(request, '1-2/karen/11-3club3.html')

def loverk(request):
	return render(request, '1-2/karen/12lover.html')

def loveropk(request):
	return render(request, '1-2/karen/13loverop.html')

def loverlovek(request):
	return render(request, '1-2/karen/14-1-1loverlove.html')

def loverlove2k(request):
	return render(request, '1-2/karen/14-1-2loverlove2.html')

def loverlove3k(request):
	return render(request, '1-2/karen/14-1-3loverlove3.html')

def lovertalkk(request):
	return render(request, '1-2/karen/14-2lovertalk.html')

def campk(request):
	return render(request, '1-2/karen/15camp.html')

def campgok(request):
	return render(request, '1-2/karen/16campgo.html')

def midtermk(request):
	return render(request, '1-2/karen/17midterm.html')

def midtermopk(request):
	return render(request, '1-2/karen/18midtermop.html')

def promk(request):
	return render(request, '1-2/karen/19prom.html')

def promgok(request):
	return render(request, '1-2/karen/20promgo.html')

def finalk(request):
	return render(request, '1-2/karen/21final.html')

def winterVacation1k(request):
	return render(request, '1-2/karen/22winterVacation1.html')

def winterVacation101k(request):
	return render(request, '1-2/karen/23-1winterVacation1-1.html')

def winterVacation102k(request):
	return render(request, '1-2/karen/23-2winterVacation1-2.html')

def winterVacationEnd1k(request):
	return render(request, '1-2/karen/24winterVacationEnd1.html')

def ktvk(request):
	return render(request, '1-2/karen/25ktv.html')

def ktvgok(request):
	return render(request, '1-2/karen/26ktvgo.html')

def secondDrop1k(request):
	return render(request, '1-2/karen/27secondDrop1.html')

def secondDrop1okk(request):
	return render(request, '1-2/karen/28secondDrop1ok.html')

def summerVacation1k(request):
	return render(request, '1-2/karen/29summerVacation1.html')

def summerVacation101k(request):
	return render(request, '1-2/karen/30-1summerVacation1-1.html')

def summerVacation102k(request):
	return render(request, '1-2/karen/30-2summerVacation1-2.html')

def summerVacation103k(request):
	return render(request, '1-2/karen/30-3summerVacation1-3.html')

def summerVacation104k(request):
	return render(request, '1-2/karen/30-4summerVacation1-4.html')

def rentHousek(request):
	return render(request, '1-2/karen/31rentHouse.html')

def sophomoreOpk(request):
	return render(request, '1-2/karen/32sophomoreOp.html')

def sophomoreOp101k(request):
	return render(request, '1-2/karen/33-1sophomoreOp1-1.html')

def sophomoreOp102k(request):
	return render(request, '1-2/karen/33-2sophomoreOp1-2.html')

def sophomoreOp103k(request):
	return render(request, '1-2/karen/33-3sophomoreOp1-3.html')

def sophomoreOp104k(request):
	return render(request, '1-2/karen/33-4sophomoreOp1-4.html')

def lover2k(request):
	return render(request, '1-2/karen/34lover2.html')

def loverop2k(request):
	return render(request, '1-2/karen/35loverop2.html')

def loverokk(request):
	return render(request, '1-2/karen/36-1loverok.html')

def loverEndk(request):
	return render(request, '1-2/karen/36-2loverEnd.html')

def secondDrop2k(request):
	return render(request, '1-2/karen/37secondDrop2.html')

def secondDrop2okk(request):
	return render(request, '1-2/karen/38secondDrop2ok.html')

def winterVacation2k(request):
	return render(request, '1-2/karen/39winterVacation2.html')

def winterVacation201k(request):
	return render(request, '1-2/karen/40-1winterVacation2-1.html')

def winterVacation202k(request):
	return render(request, '1-2/karen/40-2winterVacation2-2.html')

def sophomore2k(request):
	return render(request, '1-2/karen/41sophomore2.html')

def finalExam2k(request):
	return render(request, '1-2/karen/42finalExam2.html')

def summerVacation2k(request):
	return render(request, '1-2/karen/43summerVacation2.html')

def summerVacation201k(request):
	return render(request, '1-2/karen/44-1summerVacation2-1.html')

def summerVacation202k(request):
	return render(request, '1-2/karen/44-2summerVacation2-2.html')

def summerVacation203k(request):
	return render(request, '1-2/karen/44-3summerVacation2-3.html')

def summerVacation204k(request):
	return render(request, '1-2/karen/44-4summerVacation2-4.html')

#emico 3-4

def rdGradek(request):
	return render(request, '3-4/karen/45_3rdGrade.html')

def rdGradeOpk(request):
	return render(request, '3-4/karen/46_3rdGradeOp.html')

def exchangeOpk(request):
	return render(request, '3-4/karen/47_exchangeOp.html')

def countriesOpk(request):
	return render(request, '3-4/karen/47-1_countriesOp.html')

def USAk(request):
	return render(request, '3-4/karen/47-1-1_USA.html')

def Australiak(request):
	return render(request, '3-4/karen/47-1-2_Australia.html')

def Germanyk(request):
	return render(request, '3-4/karen/47-1-3_Germany.html')

def Francek(request):
	return render(request, '3-4/karen/47-1-4_France.html')

def exchangeNk(request):
	return render(request, '3-4/karen/47-2_exchangeN.html')

def exchangeYk(request):
	return render(request, '3-4/karen/48_exchangeY.html')

def volleyballCaptonOpk(request):
	return render(request, '3-4/karen/49_volleyballCaptonOp.html')

def captonYk(request):
	return render(request, '3-4/karen/49-1_captonY.html')

def captonNk(request):
	return render(request, '3-4/karen/49-2_captonN.html')

def summerVacation3Opk(request):
	return render(request, '3-4/karen/50_summerVacation3Op.html')

def summerVacation31k(request):
	return render(request, '3-4/karen/50-1_summerVacation3.html')

def summerVacation32k(request):
	return render(request, '3-4/karen/50-2_summerVacation3.html')

def summerVacation33k(request):
	return render(request, '3-4/karen/50-3_summerVacation3.html')

def summerVacation34k(request):
	return render(request, '3-4/karen/50-4_summerVacation3.html')

def seniork(request):
	return render(request, '3-4/karen/51_senior.html')

def seniorOpk(request):
	return render(request, '3-4/karen/52_seniorOp.html')

def internshipOpk(request):
	return render(request, '3-4/karen/52-1_internshipOp.html')

def masterOpk(request):
	return render(request, '3-4/karen/52-2_masterOp.html')

def takeExamk(request):
	return render(request, '3-4/karen/53_takeExam.html')

def workk(request):
	return render(request, '3-4/karen/53_work.html')

def finalExamOpk(request):
	return render(request, '3-4/karen/54_finalExamOp.html')

def graduationk(request):
	return render(request, '3-4/karen/55_graduation.html')

def finishGamek(request):
	return render(request, '3-4/karen/56_finishGame.html')







#timmy first and second grade

def startt(request):
	return render(request, '1-2/timmy/1start.html')

def eatopt(request):
	return render(request, '1-2/timmy/2eatop.html')

def eatgoodt(request):
	return render(request, '1-2/timmy/3-1eatgood.html')

def eatgood2t(request):
	return render(request, '1-2/timmy/3-2eatgood2.html')

def eatgood3t(request):
	return render(request, '1-2/timmy/3-3eatgood3.html')

def eatnot(request):
	return render(request, '1-2/timmy/3-4eatno.html')

def class1t(request):
	return render(request, '1-2/timmy/4class.html')

def classopt(request):
	return render(request, '1-2/timmy/5classop.html')

def classbookt(request):
	return render(request, '1-2/timmy/6-1classbook.html')

def classvideot(request):
	return render(request, '1-2/timmy/6-2classvideo.html')

def classsleept(request):
	return render(request, '1-2/timmy/6-3classsleep.html')

def homet(request):
	return render(request, '1-2/timmy/7home.html')

def homeopt(request):
	return render(request, '1-2/timmy/8homeop.html')

def homeop101t(request):
	return render(request, '1-2/timmy/9-1homeop1-1.html')

def eatgood4t(request):
	return render(request, '1-2/timmy/9-2-1eatgood4.html')

def eatgood5t(request):
	return render(request, '1-2/timmy/9-2-2eatgood5.html')

def eatgood6t(request):
	return render(request, '1-2/timmy/9-2-3eatgood6.html')

def eatgood7t(request):
	return render(request, '1-2/timmy/9-2-4eatgood7.html')

def eatop2t(request):
	return render(request, '1-2/timmy/9-2eatop2.html')

def homeop103t(request):
	return render(request, '1-2/timmy/9-3homeop1-3.html')

def homeop104t(request):
	return render(request, '1-2/timmy/9-4homeop1-4.html')

def clubt(request):
	return render(request, '1-2/timmy/10club.html')

def club1t(request):
	return render(request, '1-2/timmy/11-1club1.html')

def club2t(request):
	return render(request, '1-2/timmy/11-2club2.html')

def club3t(request):
	return render(request, '1-2/timmy/11-3club3.html')

def lovert(request):
	return render(request, '1-2/timmy/12lover.html')

def loveropt(request):
	return render(request, '1-2/timmy/13loverop.html')

def loverlovet(request):
	return render(request, '1-2/timmy/14-1-1loverlove.html')

def loverlove2t(request):
	return render(request, '1-2/timmy/14-1-2loverlove2.html')

def loverlove3t(request):
	return render(request, '1-2/timmy/14-1-3loverlove3.html')

def lovertalkt(request):
	return render(request, '1-2/timmy/14-2lovertalk.html')

def campt(request):
	return render(request, '1-2/timmy/15camp.html')

def campgot(request):
	return render(request, '1-2/timmy/16campgo.html')

def midtermt(request):
	return render(request, '1-2/timmy/17midterm.html')

def midtermopt(request):
	return render(request, '1-2/timmy/18midtermop.html')

def promt(request):
	return render(request, '1-2/timmy/19prom.html')

def promgot(request):
	return render(request, '1-2/timmy/20promgo.html')

def finalt(request):
	return render(request, '1-2/timmy/21final.html')

def winterVacation1t(request):
	return render(request, '1-2/timmy/22winterVacation1.html')

def winterVacation101t(request):
	return render(request, '1-2/timmy/23-1winterVacation1-1.html')

def winterVacation102t(request):
	return render(request, '1-2/timmy/23-2winterVacation1-2.html')

def winterVacationEnd1t(request):
	return render(request, '1-2/timmy/24winterVacationEnd1.html')

def ktvt(request):
	return render(request, '1-2/timmy/25ktv.html')

def ktvgot(request):
	return render(request, '1-2/timmy/26ktvgo.html')

def secondDrop1t(request):
	return render(request, '1-2/timmy/27secondDrop1.html')

def secondDrop1okt(request):
	return render(request, '1-2/timmy/28secondDrop1ok.html')

def summerVacation1t(request):
	return render(request, '1-2/timmy/29summerVacation1.html')

def summerVacation101t(request):
	return render(request, '1-2/timmy/30-1summerVacation1-1.html')

def summerVacation102t(request):
	return render(request, '1-2/timmy/30-2summerVacation1-2.html')

def summerVacation103t(request):
	return render(request, '1-2/timmy/30-3summerVacation1-3.html')

def summerVacation104t(request):
	return render(request, '1-2/timmy/30-4summerVacation1-4.html')

def rentHouset(request):
	return render(request, '1-2/timmy/31rentHouse.html')

def sophomoreOpt(request):
	return render(request, '1-2/timmy/32sophomoreOp.html')

def sophomoreOp101t(request):
	return render(request, '1-2/timmy/33-1sophomoreOp1-1.html')

def sophomoreOp102t(request):
	return render(request, '1-2/timmy/33-2sophomoreOp1-2.html')

def sophomoreOp103t(request):
	return render(request, '1-2/timmy/33-3sophomoreOp1-3.html')

def sophomoreOp104t(request):
	return render(request, '1-2/timmy/33-4sophomoreOp1-4.html')

def lover2t(request):
	return render(request, '1-2/timmy/34lover2.html')

def loverop2t(request):
	return render(request, '1-2/timmy/35loverop2.html')

def loverokt(request):
	return render(request, '1-2/timmy/36-1loverok.html')

def loverEndt(request):
	return render(request, '1-2/timmy/36-2loverEnd.html')

def secondDrop2t(request):
	return render(request, '1-2/timmy/37secondDrop2.html')

def secondDrop2okt(request):
	return render(request, '1-2/timmy/38secondDrop2ok.html')

def winterVacation2t(request):
	return render(request, '1-2/timmy/39winterVacation2.html')

def winterVacation201t(request):
	return render(request, '1-2/timmy/40-1winterVacation2-1.html')

def winterVacation202t(request):
	return render(request, '1-2/timmy/40-2winterVacation2-2.html')

def sophomore2t(request):
	return render(request, '1-2/timmy/41sophomore2.html')

def finalExam2t(request):
	return render(request, '1-2/timmy/42finalExam2.html')

def summerVacation2t(request):
	return render(request, '1-2/timmy/43summerVacation2.html')

def summerVacation201t(request):
	return render(request, '1-2/timmy/44-1summerVacation2-1.html')

def summerVacation202t(request):
	return render(request, '1-2/timmy/44-2summerVacation2-2.html')

def summerVacation203t(request):
	return render(request, '1-2/timmy/44-3summerVacation2-3.html')

def summerVacation204t(request):
	return render(request, '1-2/timmy/44-4summerVacation2-4.html')

#timmy third and forth grade

def rdGradet(request):
	return render(request, '3-4/timmy/45_3rdGrade.html')

def rdGradeOpt(request):
	return render(request, '3-4/timmy/46_3rdGradeOp.html')

def exchangeOpt(request):
	return render(request, '3-4/timmy/47_exchangeOp.html')

def countriesOpt(request):
	return render(request, '3-4/timmy/47-1_countriesOp.html')

def USAt(request):
	return render(request, '3-4/timmy/47-1-1_USA.html')

def Australiat(request):
	return render(request, '3-4/timmy/47-1-2_Australia.html')

def Germanyt(request):
	return render(request, '3-4/timmy/47-1-3_Germany.html')

def Francet(request):
	return render(request, '3-4/timmy/47-1-4_France.html')

def exchangeNt(request):
	return render(request, '3-4/timmy/47-2_exchangeN.html')

def exchangeYt(request):
	return render(request, '3-4/timmy/48_exchangeY.html')

def volleyballCaptonOpt(request):
	return render(request, '3-4/timmy/49_volleyballCaptonOp.html')

def captonYt(request):
	return render(request, '3-4/timmy/49-1_captonY.html')

def captonNt(request):
	return render(request, '3-4/timmy/49-2_captonN.html')

def summerVacation3Opt(request):
	return render(request, '3-4/timmy/50_summerVacation3Op.html')

def summerVacation31t(request):
	return render(request, '3-4/timmy/50-1_summerVacation3.html')

def summerVacation32t(request):
	return render(request, '3-4/timmy/50-2_summerVacation3.html')

def summerVacation33t(request):
	return render(request, '3-4/timmy/50-3_summerVacation3.html')

def summerVacation34t(request):
	return render(request, '3-4/timmy/50-4_summerVacation3.html')

def seniort(request):
	return render(request, '3-4/timmy/51_senior.html')

def seniorOpt(request):
	return render(request, '3-4/timmy/52_seniorOp.html')

def internshipOpt(request):
	return render(request, '3-4/timmy/52-1_internshipOp.html')

def masterOpt(request):
	return render(request, '3-4/timmy/52-2_masterOp.html')

def takeExamt(request):
	return render(request, '3-4/timmy/53_takeExam.html')

def workt(request):
	return render(request, '3-4/timmy/53_work.html')

def finalExamOpt(request):
	return render(request, '3-4/timmy/54_finalExamOp.html')

def graduationt(request):
	return render(request, '3-4/timmy/55_graduation.html')

def finishGamet(request):
	return render(request, '3-4/timmy/56_finishGame.html')





