from flask import Flask, render_template, request, flash, redirect, session, g, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# from forms import 
# from models import

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdef"


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///anki-deck"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

db, connect_db

