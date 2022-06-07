from django.db import models



class Base(models.Model):
    survived = models.BooleanField('Sobreviveu')
    pclass = models.IntegerField('Classe')
    sex = models.CharField(
        'Sexo',
        max_length=10,
        choices=(
            ('male','male'),
            ('female','female')
        )
    )
    age = models.IntegerField('Idade')
    name = models.TextField('Nome Completo')
    sibsp = models.IntegerField('Número de parentes a bordo')
    parch = models.IntegerField('Números de pais e filhos a bordo')
    fare = models.FloatField('Valor Passagem')
    embarked = models.CharField(
        'Embarcou',
        max_length=1,
        choices=(
            ('C','Cherbourg'),
            ('Q','Queenstown'),
            ('S','Southampton')
        )
    )
    #C = Cherbourg, Q = Queenstown, S = Southampton
    def __str__(self):
        return self.name 