


from flask import Flask, render_template

app = Flask(__name__)

ARQUIVO_JSON = 'medidas.json'

@app.route("/")
def hello_world():
    return render_template("login.html")


@app.route("/medidas")
def hello_world_2():
    return render_template("medidas.html")

@app.route("/orcamento")
def hello_world_3():
    return render_template("orcamento.html")

