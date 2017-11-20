# Development Document
-----------------------
## 一、开发设置
1、FSADeprecationWarning

解决方案：

将 flask-sqlalchemy 中的 "__init__.py"文件 789 行

> 'SQLALCHEMY_TRACK_MODIFICATIONS', None

设置为 True