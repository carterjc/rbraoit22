from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, os.path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)

	from .views import views

	app.register_blueprint(views, url_prefix='/')

	from .models import Student

	create_database(app)

	return app


def create_database(app):
	if os.path.exists('flaskr/' + DB_NAME):
		os.remove('flaskr/' + DB_NAME)
	if not os.path.exists('flaskr/' + DB_NAME):
		db.create_all(app=app)
		print('database created')

		from .create_db import load_data
		load_data(app, db)
		print('database populated')

