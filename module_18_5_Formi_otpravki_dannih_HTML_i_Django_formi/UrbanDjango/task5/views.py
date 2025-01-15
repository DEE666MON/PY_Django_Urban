from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ['dmit', 'petr', 'ivan']


def reg_post(request):
    form = None
    final = None
    errors = []
    check_usern = 0
    check_pass = False
    check_age = False
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for usern in users:
                if username == usern:
                    errors.append('Пользователь уже существует.')
                else:
                    check_usern += 1
            if password == repeat_password and (len(password) >= 8 and len(repeat_password) >= 8):
                check_pass = True
            else:
                errors.append('Пароли не совпадают или не соответствуют длине.')
            if int(age) >= 18:
                check_age = True
            else:
                errors.append('Вы должны быть старше 18.')
            if check_usern == len(users) and check_pass and check_age:
                final = f'Приветствуем, {username}.'
                users.append(username)
            print(username, password, repeat_password, age)
        else:
            form = UserRegister()
    info = {
        'form': form,
        'errors': errors,
        'final': final,
    }
    print("Пользователи:", users)
    print("Ошибки:", errors)
    print("Финал:", final)
    print("Информация об пользователе:", form)
    return render(request, 'fifth_task/registration_page.html', info)
