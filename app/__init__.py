from flask import Flask


app = Flask(__name__,static_folder="static/")
# app._static_folder = ""
app.config['TESTING'] = False

from app import routes