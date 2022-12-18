from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
app.config['SECRET_KEY'] = 'bf20701a8f6a885c1206ddff'

from website import routes # Important to keep this at the last
