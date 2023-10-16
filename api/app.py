from flask import Flask, render_template, send_file, request
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/ladybug.jpeg")
def get_image():
	return send_file("templates/ladybug.jpeg")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_eye = request.form.get("eye")
    return render_template("hello.html", name=input_name, age=input_age, eye=input_eye)