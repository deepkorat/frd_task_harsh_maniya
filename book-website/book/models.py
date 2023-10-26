from . import db

class Category(db.Model):
     __tablename__ = 'categories'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable=False)
     book = db.relationship('Book', backref='Category', cascade="all, delete-orphan")

     def __repr__(self):
          return f"\nID: {self.id}\nCategory: {self.name}"

class Book(db.Model):
     __tablename__ = 'book_details'

     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(255), nullable=False)
     author = db.Column(db.String(255), nullable=False)
     description = db.Column(db.String(500), nullable=False)
     price = db.Column(db.Float, nullable=False)
     image = db.Column(db.String(60), nullable=False)
     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
     # Define relationship with Category

     def __repr__(self):
          return f"\nID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nDescription: {self.description}\nPrice: {self.price}\nImage: {self.image}\nCategory: {self.category_id}"

     def __init__(self, title, author, description,price, image, category_id):
          self.title = title
          self.author = author
          self.description = description
          self.price = price
          self.image = image
          self.category_id = category_id


class Order(db.Model):
     __tablename__ = 'orders'
     
     id = db.Column(db.Integer, primary_key=True)
     status = db.Column(db.Boolean, default=False)
     firstname = db.Column(db.String(64))
     surname = db.Column(db.String(64))
     email = db.Column(db.String(128))
     phone = db.Column(db.String(32))
     total_cost = db.Column(db.Float)
     date = db.Column(db.DateTime)

     customer_name = db.Column(db.String(255), nullable=False)

     def __init__(self, ):
          self.customer_name = customer_name


class OrderDetail(db.Model):
     __tablename__ = 'order_details'

     id = db.Column(db.Integer, primary_key=True)
     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
     book_id = db.Column(db.Integer, db.ForeignKey('book_details.id'), nullable=False)
     quantity = db.Column(db.Integer, nullable=False)
     # Define relationship with Order and BookDetails
     order = db.relationship('Order', backref=db.backref('order_details', lazy=True))
     book = db.relationship('Book', backref=db.backref('order_details', lazy=True))

     def __init__(self, order_id, book_id, quantity):
          self.order_id = order_id
          self.book_id = book_id
          self.quantity = quantity
