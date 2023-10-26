from flask import Flask, render_template
from flask import Blueprint
from .models import Category, Book

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
     base_category = Category.query.order_by(Category.name).all()
     return render_template('index.html', categories = base_category)

@main_bp.route('/books/<int:category_id>')
def book(category_id):
     books = Book.query.filter(Book.category_id==category_id)
     category = Category.query.filter(Category.id == category_id).first()
     return render_template('book.html', books=books, category = category)

@main_bp.route('/bookdetails/<int:book_id>')
def bookdetail(book_id):
     bookdetail = Book.query.filter(Book.id == book_id).first()
     return render_template('bookdetails.html', bookdetail=bookdetail)