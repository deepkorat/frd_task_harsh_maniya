from . import db

class Category(db.Model):
     __tablename__ = 'categories'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable=False)
     book = db.relationship('Book', backref='Category', cascade="all, delete-orphan")

     def __repr__(self):
          return f"ID: {self.id}\nCategory: {self.name}"

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
          return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nDescription: {self.description}\nPrice: {self.price}\nImage: {self.image}\nCategory: {self.category_id}"