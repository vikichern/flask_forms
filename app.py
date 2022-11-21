import json
from flask import Flask
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)
 
ar=[{"name":"betty","age":20},
{"name":"alex","age":21},
{"name":"shadi","age":15}]
 
@app.route('/')
def hello():
    return "Hello"

@app.route('/data')
def data():
    return json.dumps( ar)
 
if __name__ == '__main__':
    app.run(debug=True)