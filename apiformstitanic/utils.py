import h2o
import pandas as pd
from .apps import ApiPredictMLConfig
h2o.init()
mb = h2o.load_model(ApiPredictMLConfig.MODEL_FILE)

def predict_suvirved(
        Pclass,
        Sex,
        Age,
        SibSp,
        Parch,
        Fare,
        Embarked
):

    df = pd.DataFrame([int(Pclass),
     str(Sex), 
     int(Age), 
     int(SibSp), 
     int(Parch),
    float(Fare),
    str(Embarked)]).transpose()
    df.columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    imp = h2o.H2OFrame(df)
    y = mb.predict(imp)
    return int(y['predict'])




