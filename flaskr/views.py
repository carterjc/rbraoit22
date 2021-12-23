from flask import Blueprint, render_template, request, flash, jsonify
from .models import Student
from . import db

import datetime


views = Blueprint('views', __name__)


@views.route("/", methods=['GET'])
def view_home():
	return render_template('home.html')

@views.route("/students", methods=['GET'])
def view_students():
	students = Student.query.all()
	return render_template('students.html', students=students)

@views.route("/students/<name>", methods=["GET"])
def view_student(name):
	students =  Student.query.all()
	print(students, name)
	match = [x for x in students if x.fName.lower() + x.lName.lower() == name]
	if len(match) == 0:
		return render_template('404.html'), 404
		# return '<h1>error</h1>'
	else:  # if of length 1 or more
		match = match[0]
	return render_template('student.html', student=match)

@views.route("/clubs", methods=["GET"])
def view_clubs():
	return render_template('clubs.html')

@views.context_processor
def utility_processor():
	def make_url(fName, lName):
		return "students/" + fName.lower() + lName.lower()
	def format_birthday(birthday):
		return birthday.strftime("%B %-d, %Y")
	def get_age(birthday):
		today = datetime.date.today()
		return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
	def club_list(clubs):
		return clubs.split(",")
	return dict(
		make_url=make_url,
		format_birthday=format_birthday,
		get_age=get_age,
		club_list=club_list
	)
