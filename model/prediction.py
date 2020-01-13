import joblib
from os import path

current_dir = path.dirname(path.abspath(__file__))

class Prediction:
    PIPELINE_FILE=f'{current_dir}/pipeline.pkl'

    def __init__(self, pipeline=None):
        self.__pipeline = pipeline if pipeline else joblib.load(self.PIPELINE_FILE)

    def validate(self, documents):
        return self.__pipeline.predict(documents)

    def to(self, document):
        predicted_value = self.__pipeline.predict([document])
        return predicted_value[0]
