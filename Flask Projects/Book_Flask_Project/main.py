from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

@app.route("/")
def home():
     website = "BookStore"
     return render_template('index.html', myweb=website)
     
@app.route("/category")
def category():
     return render_template('fiction.html')

@app.route("/item_detail")
def item_detail():
     return render_template('index.html')

@app.route("/add_to_cart")
def add_to_cart():
     return render_template('add_to_cart.html')

app.run(debug=True)