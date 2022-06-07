from django.urls import path


from .views import BaseAPIView


urlpatterns = [
    path('passageiro/',BaseAPIView.as_view(),name='passageiros'),
]
