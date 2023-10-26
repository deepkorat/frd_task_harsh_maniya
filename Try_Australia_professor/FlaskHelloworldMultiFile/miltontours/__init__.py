#import flask - from the package import a module
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__) 
#create a function that creates a web application
# a web server will run this web application
def create_app():
     # this is the name of the module/package that is calling this app
    app.debug = True
    app.secret_key = "somethingsecret"
    bootstrap = Bootstrap(app)
    #add the Blueprint
    from . import views
    app.register_blueprint(views.bp)    
    
    return app
