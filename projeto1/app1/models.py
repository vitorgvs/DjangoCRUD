from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.BigIntegerField('telefone')
    email = models.EmailField('email',max_length=30)

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'