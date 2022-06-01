from flaskr import db

class Student(db.Model):
	__tablename__ = 'student'
	id = db.Column(db.Integer, primary_key=True)
	fName = db.Column(db.String)
	lName = db.Column(db.String)
	bio = db.Column(db.String)
	fav_thing = db.Column(db.String)
	email = db.Column(db.String)
	image = db.Column(db.String)
	birthday = db.Column(db.Date)
	clubs = db.Column(db.String)
	plan_after_hs = db.Column(db.String)
	college = db.Column(db.String)

class Club(db.Model):
	__tablename__ = 'club'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	website = db.Column(db.String)
	images = db.Column(db.String)

class Project(db.Model):
	__tablename__ = 'project'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	members = db.Column(db.String)
	source = db.Column(db.String)
	video_url = db.Column(db.String)
