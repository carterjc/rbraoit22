from flask import Blueprint, render_template, request, flash, jsonify
from .models import Student, Club, Project
from sqlalchemy import func

import datetime, os


views = Blueprint('views', __name__)


@views.route("/", methods=['GET'])
def view_home():
	carousel_photos = os.listdir('./flaskr/static/img/carousel')
	return render_template('home.html', photos=carousel_photos)

@views.route("/students", methods=['GET'])
def view_students():
	students = Student.query.all()
	return render_template('students.html', students=students)

@views.route("/students/<name>", methods=["GET"])
def view_student(name):
	# easier method for these parameters
	students = Student.query.all()
	match = [x for x in students if x.fName.lower() + x.lName.lower() == name]

	if len(match) == 0:
		return render_template('404.html'), 404
	else:  # if of length 1 or more
		student = match[0]
	
	return render_template('student.html', student=student)

@views.route("/projects", methods=['GET'])
def view_projects():
	projects = Project.query.all()
	return render_template('projects.html', projects=projects)

@views.route("/projects/<name>", methods=['GET'])
def view_project(name):
	project = Project.query.filter(
		Project.name == name
	).first()

	if not project:
		return render_template('404.html'), 404
	
	return render_template('project.html', project=project)

@views.route("/clubs", methods=["GET"])
def view_clubs():
	clubs =  Club.query.all()
	return render_template('clubs.html', clubs=clubs)

@views.context_processor
def utility_processor():
	def make_url(fName, lName):
		return "students/" + fName.lower() + lName.lower()
	def create_path(filename, path):
		return path + filename
	def format_birthday(birthday):
		return birthday.strftime("%B %-d, %Y")
	def get_age(birthday):
		today = datetime.date.today()
		return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
	def club_list(clubs):
		return clubs.split(",")
	def lower_and_underline(s):
		return s.lower().replace(" ", "_")
	def first_sentence(s):
		return s.split(".")[0]
	return dict(
		make_url=make_url,
		create_path=create_path,
		format_birthday=format_birthday,
		get_age=get_age,
		club_list=club_list,
		lower_and_underline=lower_and_underline,
		first_sentence=first_sentence
	)
