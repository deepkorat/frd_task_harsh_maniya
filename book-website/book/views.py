from flask import Flask, render_template
from flask import Blueprint
from .models import Category, Book

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
     category = Category.query.order_by(Category.name).all()
     print(category)
     return render_template('index.html', categories = category)

@main_bp.route('/books/<int:categoryid>')
def category():
     category = "Fiction"
     return render_template('book.html', category=category)

@main_bp.route('/tours/<int:cityid>')
def citytours(cityid):
    tours = Tour.query.filter(Tour.city_id==cityid)
    return render_template('citytours.html', tours=tours)