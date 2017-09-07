from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form)

@app.route('/')
def root():
    return "Porkulence"

@app.route('/index')
def index():
    user = {'nickname': 'Sanchez'}
    car = {'make': 'Lamborghini', 'model': 'Uracco'}
    posts = [
        {
            'author': {'nickname': 'Fumes', 'fullname': 'Frank Schmaltz'},
            'body': 'Lousy car refuses to start'
        },
        {
            'author': {'nickname': 'FlatTire', 'fullname': 'George Burns'},
            'body': 'Car caught on fire today'
        },
        {
            'author': {'nickname': 'WiperBlade', 'fullname': 'Charlie Axlerod'},
            'body': 'Horn honks randomly'
        }
    ]
    return render_template('index.html',
                            title='Cars',
                            user=user,
                            car=car,
                            posts=posts)
