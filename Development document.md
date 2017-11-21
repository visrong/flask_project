# Development Document
-----------------------
## 一、开发设置
1、FSADeprecationWarning

解决方案：

将 flask-sqlalchemy 中的 "__init__.py"文件 789 行

> 'SQLALCHEMY_TRACK_MODIFICATIONS', None

设置为 True

2、model中外键

外键可以降低开发成本，减少数据量，但是在用户量大、并发度高的时候，不建议使用外键进行关联，数据的一致性和完整性问题可以通过事务来保证。

3、会话的上下文操作

db.session.add(model)

db.session.delete(model)

db.session.commit()

当会话中出现错误时(回滚会话)：

db.session.rollback()

查询：

models.class.query.all()

models.class.query.get()