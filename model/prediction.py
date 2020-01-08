import joblib

class Prediction:
    PIPELINE_FILE='pipeline.pkl'

    def __init__(self):
        self.__pipeline = joblib.load(PIPELINE_FILE)

    def defe(self, document):
        self.__pipeline.predict(document)
