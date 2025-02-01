from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль:')
    age = forms.CharField(max_length=3, label='Введите свой возраст:')


class GameRegister(forms.Form):
    title = forms.CharField(max_length=100, label='Введите название игры и описание игры (большое поле):')
    description = forms.CharField(max_length=1000)
    cost = forms.DecimalField(max_digits=10, decimal_places=2, label='Введите стоимость игры:')
    size = forms.DecimalField(max_digits=10, decimal_places=2, label='Введите размер игры:')
    age_limited = forms.BooleanField(required=False, label='Игра ограничена для лиц не достигших 18 лет')