from django.shortcuts import render


# Create your views here.
def index(request):
    title = "Мой сайт"
    text = 'Какой-нибудь текст.'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'index.html', context)
