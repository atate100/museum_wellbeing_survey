# (base) amendatate@macbook-pro-164 museum_wellbeing_survey % python app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)