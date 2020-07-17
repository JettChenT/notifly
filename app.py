from flask import Flask, render_template, request, redirect
from flask_basicauth import BasicAuth
import os
from update import Updater

upd = Updater()

app = Flask(__name__)
basic_auth = BasicAuth(app)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('ADMIN_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('ADMIN_PASSWORD')

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/submit_message',methods=['POST'])
def submit():
    msg = request.form['msg']
    upd.add_notification(msg)
    return redirect('/')

@app.route('/admin/')
@basic_auth.required
def admin_page():
    return '</br>'.join([x.decode() for x in upd.get_notification()])

if __name__ == "__main__":
    app.run(debug=True)