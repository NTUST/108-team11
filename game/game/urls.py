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

    #
]
