from flask import Blueprint, render_template, request
from miltontours.models import Category, Book

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
     category = Category.query.all()
     return render_template('index.html', cateogries = category)

@bp.route('/secret')
def secret():
     return "<h1 style='color:yellow;'>You found Secret Page</h1>"
     
@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
     print('Firstname: {}\nSurname: {}\nPhone: {}'\
          ### For GET data request, we use .args ###
          # .format(request.args.get('firstname'), request.args.get('surname'), request.args.get('phone')))

          ### For POST data request, we use .values
          # .format(request.values.get('firstname'), request.values.get('surname'), request.values.get('phone')))

          ### No matter whether you are use GET or POST, we use .form
          .format(request.form.get('firstname'), request.form.get('surname'), request.form.get('phone')))
          
     return render_template('checkout.html')