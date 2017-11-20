import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # 数据库文件的路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # 存储migrate文件

# 激活CSRF保护
CSRF_ENABLED = True

# 激活CSRF后，建立加密的令牌，用于校验表单
SECRET_KEY = 'something'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
