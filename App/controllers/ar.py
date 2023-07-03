from App.models import Turtle
from App.database import db

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from flask import jsonify


import json

#----------Train ar model
def train_model():

    data = pd.read_csv('App/ModelTrainingData.csv')
    

    X = data[['CCW', 'CCLNT']]
    y = data['Weight (Kg)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # y_pred = model.predict(X_test)

    return model

#----------Get weight from length and width
def get_weight(length, width):

    model = train_model()
    
    dimensions = {'CCW': width, 'CCLNT': length}
    dimensions_df = pd.DataFrame([dimensions])

    weight_array = model.predict(dimensions_df)

    weight = weight_array.astype(int)
    
    return weight
