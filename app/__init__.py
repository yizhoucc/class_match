from flask import Flask


app = Flask(__name__)
app._static_folder = ""
app.config['TESTING'] = False

from app import routes