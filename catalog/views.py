from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(req):
    items = Kino.objects.all()
    items2 = Kino.objects.filter(podpiska__level ='free')
    data={'k1':items.count(),'k2':items2.count()}
    return render(req,'index.html',data)

from django.views import generic
class kinolist(generic.ListView):
    model = Kino
    paginate_by = 1

# class kinodetail(generic.DetailView):
#     model = Kino
def proverka(newcom):
    blacklist=['жопа']
    spisok=newcom.body.split()
    active=True
    num=Comment.objects.all().count()
    oldcom = Comment.objects.get(id=(num-1))

    if oldcom.body==newcom.body and oldcom.user==newcom.user:
        newcom.delete()
        active=False

    for one in spisok:
        if one in blacklist:
            newcom.delete()
            active=False

    if active:
        newcom.active=True
        newcom.save()
        # breakpoint()
    pass

def kinodetail(req,pk):
    film=Kino.objects.get(id=pk)
    comments = film.comment_set.filter(active=True)
    forma = CommentForm()
    print(req.user)
    if req.POST:
        newcom = Comment()
        newcom.body =req.POST.get('body')
        newcom.kino = film
        newcom.user = req.user
        newcom.save()
        proverka(newcom)
    data={'kino':film,'form':forma,'comments':comments}
    return render(req,'catalog/kino_detail.html', data)

class directorlist(generic.ListView):
    model = Director
    paginate_by = 1

class directordetail(generic.DetailView):
    model = Director

from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def reg(req):
    if req.POST:
        f=SignUp(req.POST)#заполненная форма
        if f.is_valid(): #нет ошибок
            f.save()
            #достаем данные из формы
            k1 = f.cleaned_data.get('username')
            k2 = f.cleaned_data.get('password1')
            k3 = f.cleaned_data.get('email')
            k4 = f.cleaned_data.get('first_name')
            k5 = f.cleaned_data.get('last_name')
            #создаем нового пользователя
            user = authenticate(username = k1, password = k2)
            newuser = User.objects.get(username=k1) #находим в табллице
            #заполняем поля
            newuser.email = k3
            newuser.first_name =k4
            newuser.last_name = k5
            newuser.save()
            #создать запись в profileUser и выдать подписку 1
            ProfileUser.objects.create(user_id=newuser.id, podpiska_id=1)

            login(req,newuser) #авто логин на сайте
            return redirect('home')
    else:
        f=SignUp()#пустая форма
    data={'forma':f}
    return render(req,'registration/registration.html', data)

def topodpiska(req, userid):
    data={}
    if req.POST:
        print(userid)
        print('ok1')
        if req.POST.get('stype'):
            stype = req.POST.get('stype')
            print(stype)
            user = User.objects.get(id=userid)
            newpodp = Podpiska.objects.get(level=stype)
            if stype=='free':
                user.profileuser.podpiska=newpodp
            elif stype=='based' and user.profileuser.balance>=1:
                user.profileuser.balance-=1
                user.profileuser.podpiska=newpodp
            elif stype=='super' and user.profileuser.balance>=5:
                user.profileuser.balance-=5
                user.profileuser.podpiska=newpodp
            user.profileuser.save()
        elif req.POST.get('summa'):
            summa=req.POST.get('summa')
            print(summa)
            user = User.objects.get(id=userid)
            user.profileuser.balance +=int(summa)
            user.profileuser.save()
    return render(req, 'podpiska.html', data)

# def plusbalance(req):
#     data={}
#     return render(req, 'podpiska.html', data)