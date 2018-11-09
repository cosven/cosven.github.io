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


@app.route('/')
def index():
    db.session.add(User(name=request.args['name']))
    time.sleep(5)
    raise RuntimeError


@app.route('/check')
def check():
    user = db.session.query(User).filter_by(name=request.args['name']).first()
    return 'ok' if user is None else 'not'


app.run()
