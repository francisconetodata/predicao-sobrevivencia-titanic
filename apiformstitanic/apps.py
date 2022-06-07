from django.apps import AppConfig
from django.conf import settings
import os

class ApiformstitanicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiformstitanic'

class ApiPredictMLConfig(AppConfig):
    name = 'apiformstitanic'
    MODEL_FILE =  os.path.join(settings.MODELS, "modelo")