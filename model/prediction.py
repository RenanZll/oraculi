import joblib
from os import path

current_dir = path.dirname(path.abspath(__file__))

class Prediction:
    PIPELINE_FILE=f'{current_dir}/pipeline.pkl'

    def __init__(self):
        self.__pipeline = joblib.load(self.PIPELINE_FILE)

    def to(self, document):
        return self.__pipeline.predict(document)
