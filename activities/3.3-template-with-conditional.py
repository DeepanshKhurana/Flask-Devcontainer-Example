from flask import Flask, render_template

app = Flask(__name__)

@app.route('/status/<status>')
def status(status):
    return render_template('3.3-status.html', status=status)