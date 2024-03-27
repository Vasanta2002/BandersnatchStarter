''' Module containing a class for a RandomForestClassifier model'''
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
from datetime import datetime



class Machine:
    '''Instantiates and fits a RandomForestClassifier to make predictions'''
    def __init__(self, df):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=['Rarity'])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        prediction = self.model.predict(feature_basis)
        confidence = self.model.predict_proba(feature_basis).max()
        return *prediction, *confidence

    def save(self, filepath):
        '''Saves model to given filepath'''
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        '''Loads and returns saved model'''
        return joblib.load(filepath)

    def info(self):
        '''Returns the name of the model and the current datetime'''
        return f"Base Model: {self.name} <br /> Timestamp: {datetime.now():%Y-%m-%d %l:%M:%S %p}"