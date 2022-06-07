from rest_framework import serializers

from .models import Base

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields= (
            "id",
            "survived",
            "pclass",
            "sex",
            "age",
            "name",
            "sibsp",
            "parch",
            "fare",
            "embarked"
        )

class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields= (
            "pclass",
            "sex",
            "age",
            "sibsp",
            "parch",
            "fare",
            "embarked"
        )