from django.urls import path


from .views import BaseAPIView, PredictAPIView


urlpatterns = [
    path('passageiro/',BaseAPIView.as_view(),name='passageiros'),
    path('predict/',PredictAPIView.as_view(),name='predict'),

]
