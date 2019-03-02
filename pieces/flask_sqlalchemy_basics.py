import time

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test_tmp'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__  = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


@app.route('/health')
def ok():
    return 'ok'


@app.route('/')
def index():
    user = db.session.query(User).filter_by(name='wen').first()
    return user.name


if __name__ == '__main__':
    app.run(port=18888)
