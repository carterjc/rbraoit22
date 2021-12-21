from .models import Student
import csv, datetime

def load_data(app, db): # app, db params
    # with open("../data/student_data.csv", newline='') as f:
    #     dat = csv.reader(f)
    #     for row in dat:
    #         print(', '.join(row))
    dummy = Student(
        fName="Carter",
        lName="Costic",
        bio="bio here",
        email="cartercostic@gmail.com",
        image="/test.png",
        birthday=datetime.date(2004, 3, 5),
        clubs="CyberPatriot"
    )
    with app.app_context():
        db.session.add(dummy)
        db.session.commit()


    # db.session.add_all(items)
    # db.session.commit()

