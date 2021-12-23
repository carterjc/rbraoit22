from .models import Student
import csv, datetime, os, os.path
import zipfile, tempfile, shutil

from wand.image import Image


def load_data(app, db): # app, db params
    # Two data sources - folder with pictures and .csv with text data
    # we want to rename the pictures and create db entries with all the corresponding data

    # if unzipped pictures exist, delete them
    try:
        shutil.rmtree("./data/pictures")
    except OSError:
        pass

    students = []

    # Extract zip file to get all pictures from Google Form
    # Gets name of zipfile (we know it contains the string "Picture to be included")
    zip_name = ''.join([x for x in os.listdir('./data') if "Picture" in x])
    # Relative directory we want all the pictures to be extracted to
    extraction_dir = "./data/pictures"
    extract_zip = zipfile.ZipFile("./data/" + zip_name, "r")  # opens zipfile, prepared to extract
    temp_dir = tempfile.mkdtemp()  # makes temp directory randomly in os

    extract_zip.extractall(temp_dir)  # extracts folder with pics to random directory
    # Looks at random directory for the same type of name (no numbers appended to the end though)
    extract_name = ''.join([x for x in os.listdir(temp_dir) if "Picture" in x])
    os.mkdir("./data/pictures")
    # Moves file from the extracted folder in the temp directory into /pictures/ in the relative data directory
    # If the file type is heic, convert to jpg
    convert_images(os.path.join(temp_dir, extract_name), extraction_dir)


    with open("./data/student_data.csv", newline='') as f:
        dat = csv.reader(f)

        for row in list(dat)[1:]:
            if row[2] != "Yes":  # if user selects 'yes' to being featured on the site
                continue

            image_loc = ''.join([x for x in os.listdir("./data/pictures") if row[3] in x])
            if image_loc != "":
                file_ext = os.path.splitext(image_loc)[1]
                old_image_loc = image_loc
                image_loc = row[3].replace(" ", "").lower() + file_ext
                os.rename("./data/pictures/" + old_image_loc, "./flaskr/static/img/students/" + image_loc)

            birthday = datetime.datetime.strptime(row[4], '%m/%d/%Y')

            placeholder = Student(
                fName=row[3].split(" ")[0], 
                lName=row[3].split(" ")[1],
                bio=row[5],
                email=row[1],
                image=image_loc,
                birthday=birthday,
                clubs=row[7].replace(", ", ",")
            )

            students.append(placeholder)

        try:
            shutil.rmtree("./data/pictures")
        except OSError:
            pass

    with app.app_context():
        db.session.add_all(students)
        db.session.commit()


def convert_images(src, dst):

    for file in os.listdir(src):
        SourceFile = src + "/" + file
        TargetFile = dst + "/" + file.replace(".heic",".jpg")

        img=Image(filename=SourceFile)
        img.format='jpg'
        img.save(filename=TargetFile)
        img.close()
