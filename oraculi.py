from flask import Flask, request
from model.prediction import Prediction
import json
import os

def create_app():
    flask_app = Flask(__name__)
    return flask_app

def load_model():
    return Prediction()

print("Start model loading...")
prediction = load_model()
print("Model loaded!")
app = create_app()
print("App created!")

@app.route('/')
def index():
    return 'Server Works!!'

@app.route('/predict', methods=['POST'])
def predict():
    document = request.json['document']
    return json.dumps(
            {'classification': prediction.to(document)}
            , ensure_ascii=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
