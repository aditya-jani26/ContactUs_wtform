from flask import Flask, render_template, request, abort
from requests import Request
from form import SignupForm
import os
import requests
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello_123456789'
app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}

@app.route('/',methods=['GET', 'POST'])
def start():
    recaptcha_site_key = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    form = SignupForm()
    if form.validate_on_submit():
        secret_response = request.form['g-recaptcha-response']
        verify_response = requests.post(  
            url='https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': app.config['RECAPTCHA_PRIVATE_KEY'],
                'response': secret_response
            }
        )
        print(verify_response.json())
        if not verify_response.json()['success'] or verify_response.json()['score'] < 0.5:
            abort(401)
        else:
            print("reCAPTCHA verification successful")
            
    return render_template('index.html', form=form, recaptcha_site_key=recaptcha_site_key)

if __name__ == '__main__':
    app.run(debug=True)

