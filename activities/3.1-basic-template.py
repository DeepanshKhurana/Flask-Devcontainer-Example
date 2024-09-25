from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('3.1-home.html', name="Alice")