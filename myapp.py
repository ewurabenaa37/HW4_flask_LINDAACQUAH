from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route ('/covid')
def tracker():
      data = dict(
            newcs=145,
            total=954,
            activ=625,
            recov=160,
            deaths=24)
      return jsonify(data)
