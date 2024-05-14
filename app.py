from flask import Flask,render_template
from form import SignupForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello_123456789'

@app.route('/',methods=['GET', 'POST'])
def start():
    form = SignupForm()
    return render_template('index.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)