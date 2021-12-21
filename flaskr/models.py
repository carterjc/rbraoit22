from flaskr import db


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fName = db.Column(db.String)
	lName = db.Column(db.String)
	bio = db.Column(db.String)
	email = db.Column(db.String)
	image = db.Column(db.String)
	birthday = db.Column(db.Date)
	clubs = db.Column(db.String)