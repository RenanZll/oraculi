from flask import Flask

def create_app():
    flask_app = Flask(__name__)
    return flask_app

app = create_app()

@app.route('/')
def index():
    return 'Server Works!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
