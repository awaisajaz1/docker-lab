from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Yoda, i am ruuning from Docker Container!'

@app.route('/about')
def about():
    return "I am Yoda data engineer in qorelogix"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
