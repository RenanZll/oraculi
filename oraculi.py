from flask import Flask, request
from model.prediction import Prediction
import json
import os

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def create_app():
    flask_app = Flask(__name__)
    return flask_app

@Memoize
def load_model():
    return Prediction()

app = create_app()
print("App created!")

@app.route('/')
def index():
    return 'Server Works!!'

@app.route('/predict', methods=['POST'])
def predict():
    document = request.json['document']
    prediction = load_model()
    return json.dumps(
            {'classification': prediction.to(document)}
            , ensure_ascii=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
