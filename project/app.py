from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/jacquelona')
def jac():
    return 'Jacquelona no Navegadô!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
