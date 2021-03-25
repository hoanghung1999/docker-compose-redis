from flask import Flask, render_template, redirect, url_for, request
import redis
from  datetime import  datetime
app = Flask(__name__)
redis_connect=redis.StrictRedis(host='redis', port=6379,db=0);

@app.route('/')
def welcome():
    timenow=datetime.now();
    redis_connect.set("userlogin","false");
    return redirect('/login')

@app.route('/home')
def home():
    redis_connect.set("userlogin","true");
    return 'Login success!'


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            redis_connect.set("userlogin","true");
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)