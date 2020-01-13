from flask import Flask, request
import os

def create_app():
    flask_app = Flask(__name__)
    return flask_app

app = create_app()

@app.route('/')
def index():
    return 'Server Works!!'

@app.route('/predict', methods=['POST'])
def predict():
    document = request.json['document']
    return = Prediction().to(document)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
