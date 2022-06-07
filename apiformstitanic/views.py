from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import FormView
from .utils import predict_suvirved

from .models import Base
from .serializers import BaseSerializer
from .forms import FormPredict

def FormPredictView(request):
    form = FormPredict(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            resposta = predict_suvirved(
                Age= form.cleaned_data['age'],
                Pclass= form.cleaned_data['pclass'],
                Sex =  form.cleaned_data['sex'],
                Parch = form.cleaned_data['parch'],
                Fare= form.cleaned_data['fare'],
                Embarked = form.cleaned_data['embarked'],
                SibSp= form.cleaned_data['sibsp']
            )
            print(resposta)
            if resposta==1:
                resposta_text = 'A pessoa estará viva.'
            else:
                resposta_text = 'A pessoa estará morta.'
    else:
        resposta_text = []
        form = FormPredict()
    return render(request, 'index.html', {'form': form,
                                          'resposta':resposta_text})

class BaseAPIView(APIView):
    """

    API da base de dados do Titanic.
    Fonte: https://www.kaggle.com/competitions/titanic
    E-mail: francisconetodata@gmail.com


    """
    def get(self,request):
        passageiro = Base.objects.all()
        serializer = BaseSerializer(passageiro, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

