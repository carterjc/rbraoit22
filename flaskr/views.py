from flask import Blueprint, render_template, request, flash, jsonify
from .models import Student
from . import db
import json

import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def view_students():
	# new_student = Student(fName="Carter", lName="Costic", bio="bio here", email="cartercostic@gmail.com", image="/test.png", birthday=datetime.datetime(2004, 3, 5), clubs="CyberPatriot")
	# db.session.add(new_student)
	# db.session.commit()
	students = Student.query.all()
	print(students)
	return render_template('students.html', students=students)
	# return "<p>st=][
	# 'dents</p>"


@views.route('/about', methods=['GET'])
def about():
	return "<h1>about</h1>"


@views.route('/students', methods=['GET'])
def test():
	return render_template('about.html', title="About")
