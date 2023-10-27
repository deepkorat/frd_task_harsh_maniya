from flask import Flask, render_template
from flask import Blueprint
# from .models import Category, Book

cosmetic_bp = Blueprint('main', __name__)


# to load data gloabally to all template
# @main_bp.context_processor
# def inject_user():
#     return dict(base_category=Category.query.order_by(Category.name).all())
    
@cosmetic_bp.route('/')
def index():
     return render_template('index.html')

@cosmetic_bp.route('/product')
def product():
    return render_template('product.html')

@cosmetic_bp.route('/category')
def category():
    return render_template('category.html')