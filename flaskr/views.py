from flask import Blueprint, render_template, request, flash, jsonify
from .models import Student
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def view_students():
	return "<p>students</p>"


@views.route('/about', methods=['GET'])
def about():
	return "<h1>about</h1>"


@views.route('/students', methods=['GET'])
def test():
	return render_template('about.html', title="About")
