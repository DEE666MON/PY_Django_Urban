from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатели"
        verbose_name_plural = "Покупатели"


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = "Игры"


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Bank(models.Model):
    FIO = models.CharField()
    balance = models.IntegerField()

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "Клиенты банка"
        verbose_name_plural = "Клиенты банка"
