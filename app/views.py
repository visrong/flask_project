from app import app, db, lm, oid
from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm
from .models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    """
    首页视图函数
    :return: 首页
    """
    user = g.user
    posts = [
        {
            'author': {'name': 'John'},
            'body': 'Beautiful day'
        },
        {
            'author': {'name': 'Susan'},
            'body': 'The Avengers movie'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler  # oid.loginhander装饰器告诉 Flask-OpenID 这是登录视图
def login():
    """
    登入视图
    :return: 登录成功或失败后的页面
    """
    # 已经登录的用户不需要进行二次登录
    if g.user is not None and g.user.is_authenticated:  # g 全局变量是一个在请求生命周期中用来存储和共享数据
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data  # flask.session 提供了一个更加复杂的服务对于存储和共享数据
        return oid.try_login(form.openid.data, ask_for=['name', 'email'])  # OpenID认证异步发生
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    """
    从数据库加载用户
    :param id: 用户id
    :return: 根据用户id从数据看查出的记录
    """
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        name = resp.name
        if name is None or name == "":
            name = resp.email.split('@')[0]
        user = User(name=name, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
