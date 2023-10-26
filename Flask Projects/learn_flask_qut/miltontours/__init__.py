from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
     app=Flask(__name__)
     app.debug=True

     app.secret_key = 'BetterSecretNeeded123'
     
     #set the app configuration data 
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milton.sqlite'

     #initialise db with flask app
     db.init_app(app)

     # add the blueprint
     from . import views
     app.register_blueprint(views.bp)

     return app