from django import forms


class FormPredict(forms.Form):
    pclass = forms.IntegerField(label='Classe')
    sex = forms.ChoiceField(
        label='Sexo',
        choices=(
            ('male','male'),
            ('female','female')
        )
    )
    age = forms.IntegerField(label='Idade')
    sibsp = forms.IntegerField(label='Número de parentes a bordo')
    parch = forms.IntegerField(label='Números de pais e filhos a bordo')
    fare = forms.FloatField(label='Valor Passagem')
    embarked = forms.ChoiceField(
        label='Embarcou',
        choices=(
            ('C','Cherbourg'),
            ('Q','Queenstown'),
            ('S','Southampton')
        )
    )