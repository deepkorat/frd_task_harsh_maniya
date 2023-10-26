'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltonBooks package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltonBooks import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or Books table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Category, Book
import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
    Category1 = Category(name='Fiction')
    Category2 = Category(name='Non-Fiction')
    Category3 = Category(name='Classic Literature')
    Category4 = Category(name='Poetry')
    
    try:
        db.session.add(Category1)
        db.session.add(Category2)
        db.session.add(Category3)
        db.session.add(Category4)
        db.session.commit()
    except:
        return 'Oops!! There was an issue adding the Cateogy in dbseed function'

    book1 = Book(category_id=Category1.id,\
        title= 'Atomic Habit',\
        author= 'James Clear',\
        description= 'Tiny Changes, Remarkable Results. An Easy & Proven Way to Build a Good Habits & Break bad ones.',\
        price=300.99,\
        image='fiction-1.jpg')

    book2 = Book(category_id=Category1.id,\
        title= 'Believe in Yourself',\
        author= 'Dr. Joseph Murphy',\
        description= 'The author points out various ways by which one can overcome defeat, hardships and keep on the righteous track to succeed by using only fair means. People who are low in confidence, need a direction in life or a guiding light to keep them motivated makes this subjective compulsion a key to success for any individual says the author.',\
        price=159.99,\
        image='fiction-2.jpg')

    book3 = Book(category_id=Category1.id,\
        title= 'Rich Dad Poor Dad',\
        author= 'Robert T. Kiyosaki',\
        description= 'While so much in our world is changing a high speed, the lessons about money and the principles of Rich Dad Poor Dad haven’t changed. Today, as money continues to play a key role in our daily lives, the messages in Robert Kiyosaki’s international bestseller are more timely and more important than ever.',\
        price=400.99,\
        image='fiction-3.jpg')

    book4 = Book(category_id=Category2.id,\
        title= 'Memory: How To Develop, Train, And Use It',\
        author= 'William Walker Atkinson',\
        description= 'The book, venturing into how to mentally influence others, is an informative guide that will enable us to further our retention power, making memorizing faster and effortless.',\
        price=299.99,\
        image='non-fiction-1.jpg')

    book5 = Book(category_id=Category2.id,\
        title= 'The Power of A Positive Attitude: Your Road To Success',\
        author= 'Roger Fritz',\
        description= 'Packed with powerful information, The power of a positive attitude will help you uncover your hidden abilities and achieve success',\
        price=499.99,\
        image='non-fiction-2.jpg')

    book6 = Book(category_id=Category3.id,\
        title= 'WINGS OF FIRE',\
        author= 'Apj Abdul Kalam',\
        description= 'Summary of the Book One of the most inspiring and popular autobiographies to read is Late Abdul Kalam’s Wings of Fire. In this book, the former president shares his personal experiences and minutest details of his life.',\
        price=450.00,\
        image='classic-1.jpg')

    book7 = Book(category_id=Category3.id,\
        title= 'The Alchemist',\
        author= 'Pauro Coelho',\
        description= 'The grate story of one Child who wants Empire and how he achieve it.',\
        price=150.00,\
        image='classic-2.jpg')

    book8 = Book(category_id=Category4.id,\
        title= 'Greatest Poetry Ever Written ',\
        author= 'Grapevine',\
        description= 'Poetry gives meaning to our lives. For many of us, its a way of understanding the world around us. This book is an attempt to bring together the greatest words ever written by some men and women to have walked this planet.',\
        price=100.00,\
        image='poetry-1.jpg')

    
    try:
        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)
        db.session.add(book4)
        db.session.add(book5)
        db.session.add(book6)
        db.session.add(book7)
        db.session.add(book8)

        db.session.commit()
    except:
        return 'There was an issue adding a Book in dbseed function'

    return 'DATA LOADED'