import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    # clear all files from uploads directory
    headline = "Image Classifier web application"
    description = "Upload a picture of a flower and find out its name!"
    return render_template("index.html", headline=headline, description=description)

@app.route("/upload")
def upload():
    # get picture of flower
    # get topk from predict
    # get a name of flower from topk and get description

    headline = "Flower name"
    description = "Flower description"
    return render_template("index.html", headline=headline, description=description)