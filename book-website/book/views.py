from flask import Flask, render_template
from flask import Blueprint
from .models import Category, Book

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
     # category = Category.query.order_by(Category.name).all()
     category = ['ficiotn', 'none', '2 min kham']
     return render_template('index.html', categories = category)

@main_bp.route('/category')
def category():
     category = "Fiction"
     return render_template('fiction.html', category=category)