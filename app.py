from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
