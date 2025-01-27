from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def index(request):
    title = "Мой сайт"
    text = 'Какой-нибудь текст.'
    Buyers = Buyer.objects.all()
    Games = Game.objects.all()
    context = {
        'title': title,
        'text': text,
        'Buyers': Buyers,
        'Games': Games,
    }
    return render(request, 'index.html', context)


def plat_shop(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'plat_shop.html', context)


def reg_post_user(request):
    form = None
    final = None
    errors = []
    check_usern = 0
    check_pass = False
    check_age = False
    Buyers = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            for buyer in Buyers:
                if username == buyer.name:
                    errors.append('Пользователь уже существует.')
                else:
                    check_usern += 1
            if password == repeat_password and (len(password) >= 8 and len(repeat_password) >= 8):
                check_pass = True
            else:
                errors.append('Пароли не совпадают или не соответствуют длине.')
            if age >= 18:
                check_age = True
            else:
                errors.append('Вы должны быть старше 18.')
            if check_usern == Buyer.objects.count() and check_pass and check_age:
                final = f'Приветствуем, {username}.'
                Buyer.objects.create(name=username, balance=1000, age=age)
            print(f"U:{username}, P:{password}, RP:{repeat_password}, A:{age}")
        else:
            form = UserRegister()
    info = {
        'form': form,
        'errors': errors,
        'final': final,
        'Buyers': Buyers,
    }
    print("Пользователи:", Buyers)
    print("Ошибки:", errors)
    print("Финал:", final)
    return render(request, 'user_registration_page.html', info)


def reg_post_game(request):
    form = None
    final = None
    errors = []
    check_title = 0
    Games = Game.objects.all()
    if request.method == 'POST':
        form = GameRegister(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cost = float(form.cleaned_data['cost'])
            size = float(form.cleaned_data['size'])
            age_limited = bool(form.cleaned_data['age_limited'])
            for game in Games:
                if title == game.title:
                    errors.append('Игра уже существует.')
                else:
                    check_title += 1
            if check_title == Game.objects.count():
                final = f'Игра добавлена, {title}.'
                Game.objects.create(title=title, description=description, cost=cost, size=size, age_limited=age_limited)
            print(f"T:{title}, D:{description}, C:{cost}, S:{size}, A:{age_limited}")
        else:
            form = UserRegister()
    info = {
        'form': form,
        'errors': errors,
        'final': final,
        'Games': Games,
    }
    print("Игры:", Games)
    print("Ошибки:", errors)
    print("Финал:", final)
    return render(request, 'game_registration_page.html', info)
