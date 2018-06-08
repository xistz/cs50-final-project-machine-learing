import os
from flask import Flask, render_template, request
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename("uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    # clear all files from uploads directory
    instruction = "Upload a picture of a flower and find out its name!"
    return render_template("index.html", instruction=instruction, show_picture=False)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    # get picture of flower
    # get topk from predict
    # get a name of flower from topk and get description
    if request.method == "POST":
        # check if there is a file being uploaded
        picture = request.files["file"]
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
            picture="#",
            description=description
            )
    instruction = "Please choose a picture of a flower to upload!"
    return render_template("index.html", instruction=instruction)