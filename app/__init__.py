from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
#初始化数据库
db = SQLAlchemy(app)

from app import views,models