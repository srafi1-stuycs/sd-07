# Shakil Rafi
# SoftDev pd7
# HW07 -- Do I Know You?
# 2017-10-04

from flask import Flask, render_template, request, session, redirect
import os
app = Flask(__name__)
app.secret_key = os.urandom(32);

@app.route('/')
def home():
    if not 'logged_in' in session:
        session['logged_in'] = False
    if session.get('logged_in'):
        return render_template('index.html')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect('/')
    if str(request.form.get('username')) + str(request.form.get('password')) == '':
        error = 'Please enter both your username and password'
        return render_template('login.html',
                error=error)
    if request.form.get('username') != 'user':
        error = 'That username is not registered'
        return render_template("login.html",
                error=error)
    if request.form.get('password') != 'password':
        error = 'Incorrect password'
        return render_template('login.html',
                error=error)
    session['logged_in'] = True
    session['username'] = request.form.get('username')
    return redirect('/')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
