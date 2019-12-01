from flask import Flask
import os

def create_app():
    flask_app = Flask(__name__)
    return flask_app

app = create_app()

@app.route('/')
def index():
    return 'Server Works!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
