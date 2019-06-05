"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from mysite.views import *
from mysite import views


import mysite.views

urlpatterns = [
    #url for login



    url(r'^$', homePage),
    url(r'^startGame/', startGame, name="startGame"),
    url(r'^admin/', admin.site.urls),
    url(r'^selectCharactor/', views.selectCharactor, name="selectCharactor"),
    url(r'^gameIntroduction/', views.gameIntroduction, name="gameIntroduction"),
    url(r'^teamIntroduction/', views.teamIntroduction, name="teamIntroduction"),
    url(r'^settings1/', views.settings1, name="settings1"),
    url(r'^settings2/', views.settings2, name="settings2"),
    url(r'^settings3/', views.settings3, name="settings3"),
    url(r'^settings4/', views.settings4, name="settings4"),

    #url for emico in first and second grade

    url(r'^start/', views.start, name="start"),
    url(r'^eatop/', views.eatop, name="eatop"),
    url(r'^eatgood/', views.eatgood, name="eatgood"),
    url(r'^eatgood2/', views.eatgood2, name="eatgood2"),
    url(r'^eatgood3/', views.eatgood3, name="eatgood3"),
    url(r'^eatno/', views.eatno, name="eatno"),
    url(r'^class1/', views.class1, name="class1"),
    url(r'^classop/', views.classop, name="classop"),
    url(r'^classbook/', views.classbook, name="classbook"),
    url(r'^classvideo/', views.classvideo, name="classvideo"),
    url(r'^classsleep/', views.classsleep, name="classsleep"),
    url(r'^home/', views.home, name="home"),
    url(r'^homeop/', views.homeop, name="homeop"),
    url(r'^homeop101/', views.homeop101, name="homeop101"),
    url(r'^eatgood4/', views.eatgood4, name="eatgood4"),
    url(r'^eatgood5/', views.eatgood5, name="eatgood5"),
    url(r'^eatgood6/', views.eatgood6, name="eatgood6"),
    url(r'^eatgood7/', views.eatgood7, name="eatgood7"),
    url(r'^eatop2/', views.eatop2, name="eatop2"),
    url(r'^homeop103/', views.homeop103, name="homeop103"),
    url(r'^homeop104/', views.homeop104, name="homeop104"),
    url(r'^club/', views.club, name="club"),
    url(r'^club1/', views.club1, name="club1"),
    url(r'^club2/', views.club2, name="club2"),
    url(r'^club3/', views.club3, name="club3"),
    url(r'^lover/', views.lover, name="lover"),
    url(r'^loverop/', views.loverop, name="loverop"),
    url(r'^loverlove/', views.loverlove, name="loverlove"),
    url(r'^loverlove2/', views.loverlove2, name="loverlove2"),
    url(r'^loverlove3/', views.loverlove3, name="loverlove3"),
    url(r'^lovertalk/', views.lovertalk, name="lovertalk"),
    url(r'^camp/', views.camp, name="camp"),
    url(r'^campgo/', views.campgo, name="campgo"),
    url(r'^midterm/', views.midterm, name="midterm"),
    url(r'^midtermop/', views.midtermop, name="midtermop"),
    url(r'^prom/', views.prom, name="prom"),
    url(r'^promgo/', views.promgo, name="promgo"),
    url(r'^final/', views.final, name="final"),
    url(r'^winterVacation1/', views.winterVacation1, name="winterVacation1"),
    url(r'^winterVacation101/', views.winterVacation101, name="winterVacation101"),
    url(r'^winterVacation102/', views.winterVacation102, name="winterVacation102"),
    url(r'^winterVacationEnd1/', views.winterVacationEnd1, name="winterVacationEnd1"),
    url(r'^ktv/', views.ktv, name="ktv"),
    url(r'^ktvgo/', views.ktvgo, name="ktvgo"),
    url(r'^secondDrop1/', views.secondDrop1, name="secondDrop1"),
    url(r'^secondDrop1ok/', views.secondDrop1ok, name="secondDrop1ok"),
    url(r'^summerVacation1/', views.summerVacation1, name="summerVacation1"),
    url(r'^summerVacation101/', views.summerVacation101, name="summerVacation101"),
    url(r'^summerVacation102/', views.summerVacation102, name="summerVacation102"),
    url(r'^summerVacation103/', views.summerVacation103, name="summerVacation103"),
    url(r'^summerVacation104/', views.summerVacation104, name="summerVacation104"),
    url(r'^rentHouse/', views.rentHouse, name="rentHouse"),
    url(r'^sophomoreOp/', views.sophomoreOp, name="sophomoreOp"),
    url(r'^sophomoreOp101/', views.sophomoreOp101, name="sophomoreOp101"),
    url(r'^sophomoreOp102/', views.sophomoreOp102, name="sophomoreOp102"),
    url(r'^sophomoreOp103/', views.sophomoreOp103, name="sophomoreOp103"),
    url(r'^sophomoreOp104/', views.sophomoreOp104, name="sophomoreOp104"),
    url(r'^lover2/', views.lover2, name="lover2"),
    url(r'^loverop2/', views.loverop2, name="loverop2"),
    url(r'^loverok/', views.loverok, name="loverok"),
    url(r'^loverEnd/', views.loverEnd, name="loverEnd"),
    url(r'^secondDrop2/', views.secondDrop2, name="secondDrop2"),
    url(r'^secondDrop2ok/', views.secondDrop2ok, name="secondDrop2ok"),
    url(r'^winterVacation2/', views.winterVacation2, name="winterVacation2"),
    url(r'^winterVacation201/', views.winterVacation201, name="winterVacation201"),
    url(r'^winterVacation202/', views.winterVacation202, name="winterVacation202"),
    url(r'^sophomore2/', views.sophomore2, name="sophomore2"),
    url(r'^finalExam2/', views.finalExam2, name="finalExam2"),
    url(r'^summerVacation2/', views.summerVacation2, name="summerVacation2"),
    url(r'^summerVacation201/', views.summerVacation201, name="summerVacation201"),
    url(r'^summerVacation202/', views.summerVacation202, name="summerVacation202"),
    url(r'^summerVacation203/', views.summerVacation203, name="summerVacation203"),
    url(r'^summerVacation204/', views.summerVacation204, name="summerVacation204"),

    #url for emico in third and forth grade

    url(r'^rdGrade/', views.rdGrade, name="rdGrade"),
    url(r'^rdGradeOp/', views.rdGradeOp, name="rdGradeOp"),
    url(r'^exchangeOp/', views.exchangeOp, name="exchangeOp"),
    url(r'^countriesOp/', views.countriesOp, name="countriesOp"),
    url(r'^USA/', views.USA, name="USA"),
    url(r'^Australia/', views.Australia, name="Australia"),
    url(r'^Germany/', views.Germany, name="Germany"),
    url(r'^France/', views.France, name="France"),
    url(r'^exchangeN/', views.exchangeN, name="exchangeN"),
    url(r'^exchangeY/', views.exchangeY, name="exchangeY"),
    url(r'^volleyballCaptonOp/', views.volleyballCaptonOp, name="volleyballCaptonOp"),
    url(r'^captonY/', views.captonY, name="captonY"),
    url(r'^captonN/', views.captonN, name="captonN"),
    url(r'^summerVacation3Op/', views.summerVacation3Op, name="summerVacation3Op"),
    url(r'^summerVacation31/', views.summerVacation31, name="summerVacation31"),
    url(r'^summerVacation32/', views.summerVacation32, name="summerVacation32"),
    url(r'^summerVacation33/', views.summerVacation33, name="summerVacation33"),
    url(r'^summerVacation34/', views.summerVacation34, name="summerVacation34"),
    url(r'^senior/', views.senior, name="senior"),
    url(r'^seniorOp/', views.seniorOp, name="seniorOp"),
    url(r'^internshipOp/', views.internshipOp, name="internshipOp"),
    url(r'^masterOp/', views.masterOp, name="masterOp"),
    url(r'^takeExam/', views.takeExam, name="takeExam"),
    url(r'^work/', views.work, name="work"),
    url(r'^finalExamOp/', views.finalExamOp, name="finalExamOp"),
    url(r'^graduation/', views.graduation, name="graduation"),
    url(r'^finishGame/', views.finishGame, name="finishGame"),
    url(r'^gameOver/', views.gameOver, name="gameOver"),

    




    #url for karen in first and second grade

    url(r'^startk/', views.startk, name="startk"),
    url(r'^eatopk/', views.eatopk, name="eatopk"),
    url(r'^eatgoodk/', views.eatgoodk, name="eatgoodk"),
    url(r'^eatgood2k/', views.eatgood2k, name="eatgood2k"),
    url(r'^eatgood3k/', views.eatgood3k, name="eatgood3k"),
    url(r'^eatnok/', views.eatnok, name="eatnok"),
    url(r'^class1k/', views.class1k, name="class1k"),
    url(r'^classopk/', views.classopk, name="classopk"),
    url(r'^classbookk/', views.classbookk, name="classbookk"),
    url(r'^classvideok/', views.classvideok, name="classvideok"),
    url(r'^classsleepk/', views.classsleepk, name="classsleepk"),
    url(r'^homek/', views.homek, name="homek"),
    url(r'^homeopk/', views.homeopk, name="homeopk"),
    url(r'^homeop101k/', views.homeop101k, name="homeop101k"),
    url(r'^eatgood4k/', views.eatgood4k, name="eatgood4k"),
    url(r'^eatgood5k/', views.eatgood5k, name="eatgood5k"),
    url(r'^eatgood6k/', views.eatgood6k, name="eatgood6k"),
    url(r'^eatgood7k/', views.eatgood7k, name="eatgood7k"),
    url(r'^eatop2k/', views.eatop2k, name="eatop2k"),
    url(r'^homeop103k/', views.homeop103k, name="homeop103k"),
    url(r'^homeop104k/', views.homeop104k, name="homeop104k"),
    url(r'^clubk/', views.clubk, name="clubk"),
    url(r'^club1k/', views.club1k, name="club1k"),
    url(r'^club2k/', views.club2k, name="club2k"),
    url(r'^club3k/', views.club3k, name="club3k"),
    url(r'^loverk/', views.loverk, name="loverk"),
    url(r'^loveropk/', views.loveropk, name="loveropk"),
    url(r'^loverlovek/', views.loverlovek, name="loverlovek"),
    url(r'^loverlove2k/', views.loverlove2k, name="loverlove2k"),
    url(r'^loverlove3k/', views.loverlove3k, name="loverlove3k"),
    url(r'^lovertalkk/', views.lovertalkk, name="lovertalkk"),
    url(r'^campk/', views.campk, name="campk"),
    url(r'^campgok/', views.campgok, name="campgok"),
    url(r'^midtermk/', views.midtermk, name="midtermk"),
    url(r'^midtermopk/', views.midtermopk, name="midtermopk"),
    url(r'^promk/', views.promk, name="promk"),
    url(r'^promgok/', views.promgok, name="promgok"),
    url(r'^finalk/', views.finalk, name="finalk"),
    url(r'^winterVacation1k/', views.winterVacation1k, name="winterVacation1k"),
    url(r'^winterVacation101k/', views.winterVacation101k, name="winterVacation101k"),
    url(r'^winterVacation102k/', views.winterVacation102k, name="winterVacation102k"),
    url(r'^winterVacationEnd1k/', views.winterVacationEnd1k, name="winterVacationEnd1k"),
    url(r'^ktvk/', views.ktvk, name="ktvk"),
    url(r'^ktvgok/', views.ktvgok, name="ktvgok"),
    url(r'^secondDrop1k/', views.secondDrop1k, name="secondDrop1k"),
    url(r'^secondDrop1okk/', views.secondDrop1okk, name="secondDrop1okk"),
    url(r'^summerVacation1k/', views.summerVacation1k, name="summerVacation1k"),
    url(r'^summerVacation101k/', views.summerVacation101k, name="summerVacation101k"),
    url(r'^summerVacation102k/', views.summerVacation102k, name="summerVacation102k"),
    url(r'^summerVacation103k/', views.summerVacation103k, name="summerVacation103k"),
    url(r'^summerVacation104k/', views.summerVacation104k, name="summerVacation104k"),
    url(r'^rentHousek/', views.rentHousek, name="rentHousek"),
    url(r'^sophomoreOpk/', views.sophomoreOpk, name="sophomoreOpk"),
    url(r'^sophomoreOp101k/', views.sophomoreOp101k, name="sophomoreOp101k"),
    url(r'^sophomoreOp102k/', views.sophomoreOp102k, name="sophomoreOp102k"),
    url(r'^sophomoreOp103k/', views.sophomoreOp103k, name="sophomoreOp103k"),
    url(r'^sophomoreOp104k/', views.sophomoreOp104k, name="sophomoreOp104k"),
    url(r'^lover2k/', views.lover2k, name="lover2k"),
    url(r'^loverop2k/', views.loverop2k, name="loverop2k"),
    url(r'^loverokk/', views.loverokk, name="loverokk"),
    url(r'^loverEndk/', views.loverEndk, name="loverEndk"),
    url(r'^secondDrop2k/', views.secondDrop2k, name="secondDrop2k"),
    url(r'^secondDrop2okk/', views.secondDrop2okk, name="secondDrop2okk"),
    url(r'^winterVacation2k/', views.winterVacation2k, name="winterVacation2k"),
    url(r'^winterVacation201k/', views.winterVacation201k, name="winterVacation201k"),
    url(r'^winterVacation202k/', views.winterVacation202k, name="winterVacation202k"),
    url(r'^sophomore2k/', views.sophomore2k, name="sophomore2k"),
    url(r'^finalExam2k/', views.finalExam2k, name="finalExam2k"),
    url(r'^summerVacation2k/', views.summerVacation2k, name="summerVacation2k"),
    url(r'^summerVacation201k/', views.summerVacation201k, name="summerVacation201k"),
    url(r'^summerVacation202k/', views.summerVacation202k, name="summerVacation202k"),
    url(r'^summerVacation203k/', views.summerVacation203k, name="summerVacation203k"),
    url(r'^summerVacation204k/', views.summerVacation204k, name="summerVacation204k"),

    #url for karen in third and forth grade

    url(r'^rdGradek/', views.rdGradek, name="rdGradek"),
    url(r'^rdGradeOpk/', views.rdGradeOpk, name="rdGradeOpk"),
    url(r'^exchangeOpk/', views.exchangeOpk, name="exchangeOpk"),
    url(r'^countriesOpk/', views.countriesOpk, name="countriesOpk"),
    url(r'^USAk/', views.USAk, name="USAk"),
    url(r'^Australiak/', views.Australiak, name="Australiak"),
    url(r'^Germanyk/', views.Germanyk, name="Germanyk"),
    url(r'^Francek/', views.Francek, name="Francek"),
    url(r'^exchangeNk/', views.exchangeNk, name="exchangeNk"),
    url(r'^exchangeYk/', views.exchangeYk, name="exchangeYk"),
    url(r'^volleyballCaptonOpk/', views.volleyballCaptonOpk, name="volleyballCaptonOpk"),
    url(r'^captonYk/', views.captonYk, name="captonYk"),
    url(r'^captonNk/', views.captonNk, name="captonNk"),
    url(r'^summerVacation3Opk/', views.summerVacation3Opk, name="summerVacation3Opk"),
    url(r'^summerVacation31k/', views.summerVacation31k, name="summerVacation31k"),
    url(r'^summerVacation32k/', views.summerVacation32k, name="summerVacation32k"),
    url(r'^summerVacation33k/', views.summerVacation33k, name="summerVacation33k"),
    url(r'^summerVacation34k/', views.summerVacation34k, name="summerVacation34k"),
    url(r'^seniork/', views.seniork, name="seniork"),
    url(r'^seniorOpk/', views.seniorOpk, name="seniorOpk"),
    url(r'^internshipOpk/', views.internshipOpk, name="internshipOpk"),
    url(r'^masterOpk/', views.masterOpk, name="masterOpk"),
    url(r'^takeExamk/', views.takeExamk, name="takeExamk"),
    url(r'^workk/', views.workk, name="workk"),
    url(r'^finalExamOpk/', views.finalExamOpk, name="finalExamOpk"),
    url(r'^graduationk/', views.graduationk, name="graduationk"),
    url(r'^finishGamek/', views.finishGamek, name="finishGamek"),





    #url for timmy in first and second grade

    url(r'^startt/', views.startt, name="startt"),
    url(r'^eatopt/', views.eatopt, name="eatopt"),
    url(r'^eatgoodt/', views.eatgoodt, name="eatgoodt"),
    url(r'^eatgood2t/', views.eatgood2t, name="eatgood2t"),
    url(r'^eatgood3t/', views.eatgood3t, name="eatgood3t"),
    url(r'^eatnot/', views.eatnot, name="eatnot"),
    url(r'^class1t/', views.class1t, name="class1t"),
    url(r'^classopt/', views.classopt, name="classopt"),
    url(r'^classbookt/', views.classbookt, name="classbookt"),
    url(r'^classvideot/', views.classvideot, name="classvideot"),
    url(r'^classsleept/', views.classsleept, name="classsleept"),
    url(r'^homet/', views.homet, name="homet"),
    url(r'^homeopt/', views.homeopt, name="homeopt"),
    url(r'^homeop101t/', views.homeop101t, name="homeop101t"),
    url(r'^eatgood4t/', views.eatgood4t, name="eatgood4t"),
    url(r'^eatgood5t/', views.eatgood5t, name="eatgood5t"),
    url(r'^eatgood6t/', views.eatgood6t, name="eatgood6t"),
    url(r'^eatgood7t/', views.eatgood7t, name="eatgood7t"),
    url(r'^eatop2t/', views.eatop2t, name="eatop2t"),
    url(r'^homeop103t/', views.homeop103t, name="homeop103t"),
    url(r'^homeop104t/', views.homeop104t, name="homeop104t"),
    url(r'^clubt/', views.clubt, name="clubt"),
    url(r'^club1t/', views.club1t, name="club1t"),
    url(r'^club2t/', views.club2t, name="club2t"),
    url(r'^club3t/', views.club3t, name="club3t"),
    url(r'^lovert/', views.lovert, name="lovert"),
    url(r'^loveropt/', views.loveropt, name="loveropt"),
    url(r'^loverlovet/', views.loverlovet, name="loverlovet"),
    url(r'^loverlove2t/', views.loverlove2t, name="loverlove2t"),
    url(r'^loverlove3t/', views.loverlove3t, name="loverlove3t"),
    url(r'^lovertalkt/', views.lovertalkt, name="lovertalkt"),
    url(r'^campt/', views.campt, name="campt"),
    url(r'^campgot/', views.campgot, name="campgot"),
    url(r'^midtermt/', views.midtermt, name="midtermt"),
    url(r'^midtermopt/', views.midtermopt, name="midtermopt"),
    url(r'^promt/', views.promt, name="promt"),
    url(r'^promgot/', views.promgot, name="promgot"),
    url(r'^finalt/', views.finalt, name="finalt"),
    url(r'^winterVacation1t/', views.winterVacation1t, name="winterVacation1t"),
    url(r'^winterVacation101t/', views.winterVacation101t, name="winterVacation101t"),
    url(r'^winterVacation102t/', views.winterVacation102t, name="winterVacation102t"),
    url(r'^winterVacationEnd1t/', views.winterVacationEnd1t, name="winterVacationEnd1t"),
    url(r'^ktvt/', views.ktvt, name="ktvt"),
    url(r'^ktvgot/', views.ktvgot, name="ktvgot"),
    url(r'^secondDrop1t/', views.secondDrop1t, name="secondDrop1t"),
    url(r'^secondDrop1okt/', views.secondDrop1okt, name="secondDrop1okt"),
    url(r'^summerVacation1t/', views.summerVacation1t, name="summerVacation1t"),
    url(r'^summerVacation101t/', views.summerVacation101t, name="summerVacation101t"),
    url(r'^summerVacation102t/', views.summerVacation102t, name="summerVacation102t"),
    url(r'^summerVacation103t/', views.summerVacation103t, name="summerVacation103t"),
    url(r'^summerVacation104t/', views.summerVacation104t, name="summerVacation104t"),
    url(r'^rentHouset/', views.rentHouset, name="rentHouset"),
    url(r'^sophomoreOpt/', views.sophomoreOpt, name="sophomoreOpt"),
    url(r'^sophomoreOp101t/', views.sophomoreOp101t, name="sophomoreOp101t"),
    url(r'^sophomoreOp102t/', views.sophomoreOp102t, name="sophomoreOp102t"),
    url(r'^sophomoreOp103t/', views.sophomoreOp103t, name="sophomoreOp103t"),
    url(r'^sophomoreOp104t/', views.sophomoreOp104t, name="sophomoreOp104t"),
    url(r'^lover2t/', views.lover2t, name="lover2t"),
    url(r'^loverop2t/', views.loverop2t, name="loverop2t"),
    url(r'^loverokt/', views.loverokt, name="loverokt"),
    url(r'^loverEndt/', views.loverEndt, name="loverEndt"),
    url(r'^secondDrop2t/', views.secondDrop2t, name="secondDrop2t"),
    url(r'^secondDrop2okt/', views.secondDrop2okt, name="secondDrop2okt"),
    url(r'^winterVacation2t/', views.winterVacation2t, name="winterVacation2t"),
    url(r'^winterVacation201t/', views.winterVacation201t, name="winterVacation201t"),
    url(r'^winterVacation202t/', views.winterVacation202t, name="winterVacation202t"),
    url(r'^sophomore2t/', views.sophomore2t, name="sophomore2t"),
    url(r'^finalExam2t/', views.finalExam2t, name="finalExam2t"),
    url(r'^summerVacation2t/', views.summerVacation2t, name="summerVacation2t"),
    url(r'^summerVacation201t/', views.summerVacation201t, name="summerVacation201t"),
    url(r'^summerVacation202t/', views.summerVacation202t, name="summerVacation202t"),
    url(r'^summerVacation203t/', views.summerVacation203t, name="summerVacation203t"),
    url(r'^summerVacation204t/', views.summerVacation204t, name="summerVacation204t"),

    #url for timmy in third and forth grade

    url(r'^rdGradet/', views.rdGradet, name="rdGradet"),
    url(r'^rdGradeOpt/', views.rdGradeOpt, name="rdGradeOpt"),
    url(r'^exchangeOpt/', views.exchangeOpt, name="exchangeOpt"),
    url(r'^countriesOpt/', views.countriesOpt, name="countriesOpt"),
    url(r'^USAt/', views.USAt, name="USAt"),
    url(r'^Australiat/', views.Australiat, name="Australiat"),
    url(r'^Germanyt/', views.Germanyt, name="Germanyt"),
    url(r'^Francet/', views.Francet, name="Francet"),
    url(r'^exchangeNt/', views.exchangeNt, name="exchangeNt"),
    url(r'^exchangeYt/', views.exchangeYt, name="exchangeYt"),
    url(r'^volleyballCaptonOpt/', views.volleyballCaptonOpt, name="volleyballCaptonOpt"),
    url(r'^captonYt/', views.captonYt, name="captonYt"),
    url(r'^captonNt/', views.captonNt, name="captonNt"),
    url(r'^summerVacation3Opt/', views.summerVacation3Opt, name="summerVacation3Opt"),
    url(r'^summerVacation31t/', views.summerVacation31t, name="summerVacation31t"),
    url(r'^summerVacation32t/', views.summerVacation32t, name="summerVacation32t"),
    url(r'^summerVacation33t/', views.summerVacation33t, name="summerVacation33t"),
    url(r'^summerVacation34t/', views.summerVacation34t, name="summerVacation34t"),
    url(r'^seniort/', views.seniort, name="seniort"),
    url(r'^seniorOpt/', views.seniorOpt, name="seniorOpt"),
    url(r'^internshipOpt/', views.internshipOpt, name="internshipOpt"),
    url(r'^masterOpt/', views.masterOpt, name="masterOpt"),
    url(r'^takeExamt/', views.takeExamt, name="takeExamt"),
    url(r'^workt/', views.workt, name="workt"),
    url(r'^finalExamOpt/', views.finalExamOpt, name="finalExamOpt"),
    url(r'^graduationt/', views.graduationt, name="graduationt"),
    url(r'^finishGamet/', views.finishGamet, name="finishGamet"),



    







    #url for leo in first and second grade

    url(r'^startl/', views.startl, name="startl"),
    url(r'^eatopl/', views.eatopl, name="eatopl"),
    url(r'^eatgoodl/', views.eatgoodl, name="eatgoodl"),
    url(r'^eatgood2l/', views.eatgood2l, name="eatgood2l"),
    url(r'^eatgood3l/', views.eatgood3l, name="eatgood3l"),
    url(r'^eatnol/', views.eatnol, name="eatnol"),
    url(r'^class1l/', views.class1l, name="class1l"),
    url(r'^classopl/', views.classopl, name="classopl"),
    url(r'^classbookl/', views.classbookl, name="classbookl"),
    url(r'^classvideol/', views.classvideol, name="classvideol"),
    url(r'^classsleepl/', views.classsleepl, name="classsleepl"),
    url(r'^homel/', views.homel, name="homel"),
    url(r'^homeopl/', views.homeopl, name="homeopl"),
    url(r'^homeop101l/', views.homeop101l, name="homeop101l"),
    url(r'^eatgood4l/', views.eatgood4l, name="eatgood4l"),
    url(r'^eatgood5l/', views.eatgood5l, name="eatgood5l"),
    url(r'^eatgood6l/', views.eatgood6l, name="eatgood6l"),
    url(r'^eatgood7l/', views.eatgood7l, name="eatgood7l"),
    url(r'^eatop2l/', views.eatop2l, name="eatop2l"),
    url(r'^homeop103l/', views.homeop103l, name="homeop103l"),
    url(r'^homeop104l/', views.homeop104l, name="homeop104l"),
    url(r'^clubl/', views.clubl, name="clubl"),
    url(r'^club1l/', views.club1l, name="club1l"),
    url(r'^club2l/', views.club2l, name="club2l"),
    url(r'^club3l/', views.club3l, name="club3l"),
    url(r'^loverl/', views.loverl, name="loverl"),
    url(r'^loveropl/', views.loveropl, name="loveropl"),
    url(r'^loverlovel/', views.loverlovel, name="loverlovel"),
    url(r'^loverlove2l/', views.loverlove2l, name="loverlove2l"),
    url(r'^loverlove3l/', views.loverlove3l, name="loverlove3l"),
    url(r'^lovertalkl/', views.lovertalkl, name="lovertalkl"),
    url(r'^campl/', views.campl, name="campl"),
    url(r'^campgol/', views.campgol, name="campgol"),
    url(r'^midterml/', views.midterml, name="midterml"),
    url(r'^midtermopl/', views.midtermopl, name="midtermopl"),
    url(r'^proml/', views.proml, name="proml"),
    url(r'^promgol/', views.promgol, name="promgol"),
    url(r'^finall/', views.finall, name="finall"),
    url(r'^winterVacation1l/', views.winterVacation1l, name="winterVacation1l"),
    url(r'^winterVacation101l/', views.winterVacation101l, name="winterVacation101l"),
    url(r'^winterVacation102l/', views.winterVacation102l, name="winterVacation102l"),
    url(r'^winterVacationEnd1l/', views.winterVacationEnd1l, name="winterVacationEnd1l"),
    url(r'^ktvl/', views.ktvl, name="ktvl"),
    url(r'^ktvgol/', views.ktvgol, name="ktvgol"),
    url(r'^secondDrop1l/', views.secondDrop1l, name="secondDrop1l"),
    url(r'^secondDrop1okl/', views.secondDrop1okl, name="secondDrop1okl"),
    url(r'^summerVacation1l/', views.summerVacation1l, name="summerVacation1l"),
    url(r'^summerVacation101l/', views.summerVacation101l, name="summerVacation101l"),
    url(r'^summerVacation102l/', views.summerVacation102l, name="summerVacation102l"),
    url(r'^summerVacation103l/', views.summerVacation103l, name="summerVacation103l"),
    url(r'^summerVacation104l/', views.summerVacation104l, name="summerVacation104l"),
    url(r'^rentHousel/', views.rentHousel, name="rentHousel"),
    url(r'^sophomoreOpl/', views.sophomoreOpl, name="sophomoreOpl"),
    url(r'^sophomoreOp101l/', views.sophomoreOp101l, name="sophomoreOp101l"),
    url(r'^sophomoreOp102l/', views.sophomoreOp102l, name="sophomoreOp102l"),
    url(r'^sophomoreOp103l/', views.sophomoreOp103l, name="sophomoreOp103l"),
    url(r'^sophomoreOp104l/', views.sophomoreOp104l, name="sophomoreOp104l"),
    url(r'^lover2l/', views.lover2l, name="lover2l"),
    url(r'^loverop2l/', views.loverop2l, name="loverop2l"),
    url(r'^loverokl/', views.loverokl, name="loverokl"),
    url(r'^loverEndl/', views.loverEndl, name="loverEndl"),
    url(r'^secondDrop2l/', views.secondDrop2l, name="secondDrop2l"),
    url(r'^secondDrop2okl/', views.secondDrop2okl, name="secondDrop2okl"),
    url(r'^winterVacation2l/', views.winterVacation2l, name="winterVacation2l"),
    url(r'^winterVacation201l/', views.winterVacation201l, name="winterVacation201l"),
    url(r'^winterVacation202l/', views.winterVacation202l, name="winterVacation202l"),
    url(r'^sophomore2l/', views.sophomore2l, name="sophomore2l"),
    url(r'^finalExam2l/', views.finalExam2l, name="finalExam2l"),
    url(r'^summerVacation2l/', views.summerVacation2l, name="summerVacation2l"),
    url(r'^summerVacation201l/', views.summerVacation201l, name="summerVacation201l"),
    url(r'^summerVacation202l/', views.summerVacation202l, name="summerVacation202l"),
    url(r'^summerVacation203l/', views.summerVacation203l, name="summerVacation203l"),
    url(r'^summerVacation204l/', views.summerVacation204l, name="summerVacation204l"),

    #url for leo in third and forth grade

    url(r'^rdGradel/', views.rdGradel, name="rdGradel"),
    url(r'^rdGradeOpl/', views.rdGradeOpl, name="rdGradeOpl"),
    url(r'^exchangeOpl/', views.exchangeOpl, name="exchangeOpl"),
    url(r'^countriesOpl/', views.countriesOpl, name="countriesOpl"),
    url(r'^USAl/', views.USAl, name="USAl"),
    url(r'^Australial/', views.Australial, name="Australial"),
    url(r'^Germanyl/', views.Germanyl, name="Germanyl"),
    url(r'^Francel/', views.Francel, name="Francel"),
    url(r'^exchangeNl/', views.exchangeNl, name="exchangeNl"),
    url(r'^exchangeYl/', views.exchangeYl, name="exchangeYl"),
    url(r'^volleyballCaptonOpl/', views.volleyballCaptonOpl, name="volleyballCaptonOpl"),
    url(r'^captonYl/', views.captonYl, name="captonYl"),
    url(r'^captonNl/', views.captonNl, name="captonNl"),
    url(r'^summerVacation3Opl/', views.summerVacation3Opl, name="summerVacation3Opl"),
    url(r'^summerVacation31l/', views.summerVacation31l, name="summerVacation31l"),
    url(r'^summerVacation32l/', views.summerVacation32l, name="summerVacation32l"),
    url(r'^summerVacation33l/', views.summerVacation33l, name="summerVacation33l"),
    url(r'^summerVacation34l/', views.summerVacation34l, name="summerVacation34l"),
    url(r'^seniorl/', views.seniorl, name="seniorl"),
    url(r'^seniorOpl/', views.seniorOpl, name="seniorOpl"),
    url(r'^internshipOpl/', views.internshipOpl, name="internshipOpl"),
    url(r'^masterOpl/', views.masterOpl, name="masterOpl"),
    url(r'^takeExaml/', views.takeExaml, name="takeExaml"),
    url(r'^workl/', views.workl, name="workl"),
    url(r'^finalExamOpl/', views.finalExamOpl, name="finalExamOpl"),
    url(r'^graduationl/', views.graduationl, name="graduationl"),
    url(r'^finishGamel/', views.finishGamel, name="finishGamel"),






    ]
