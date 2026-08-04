from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/orcamento")
def hello_world_2():
    return render_template("index2.html")

