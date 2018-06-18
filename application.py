import os
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename("uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    # clear all files from uploads directory
    if request.method == "POST":
        # check if there is a file being uploaded
        picture = request.files["file"]
        # check if submitted file is a jpeg
        picture_name = os.path.join(app.config['UPLOAD_FOLDER'], picture.filename)
        picture.save(picture_name)
        name = "Flower name"
        description = "Flower description"
        instruction = "Upload another picture of a flower and find out its name!"
        return render_template(
            "index.html",
            instruction=instruction,
            show_picture=True,
            name=name,
            picture=picture_name,
            description=description
            )
    else:
        instruction = "Upload a picture of a flower and find out its name!"
        return render_template("index.html", instruction=instruction, show_picture=False)

@app.route("/uploads/<filename>")
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)