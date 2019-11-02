from flask import Flask, render_template
from flask_restful import Api
from flask_mysqldb import MySQL
from views import UserDataManagement
from models import db, ma

# Init App
app = Flask(__name__)
api = Api(app)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'newpage_test'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Config SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/newpage_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init MYSQL
mysql = MySQL(app)
db.init_app(app)
ma.init_app(app)


# Create DB with respect to app.
with app.app_context():
    db.create_all()
    db.session.commit()

#Add the URLs
api.add_resource(UserDataManagement, '/api/users')

if __name__ == '__main__':
   app.run()