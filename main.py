# Importe o "flash" do pacote flask
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# OBRIGATÓRIO PARA USAR FLASH: Define uma chave secreta para proteger as sessões
app.secret_key = "chave_secreta_super_segura_da_colortech"

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "123456"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        usuario_digitado = request.form.get("usuario")
        senha_digitada = request.form.get("senha")
        
        if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
            return redirect(url_for("pagina_principal"))
        else:
            # Envia a mensagem de erro que será capturada pelo HTML
            flash("Usuário ou senha incorretos!", "error")
            return render_template("index.html")
            
    return render_template("index.html")


@app.route("/medidas")
def pagina_principal():
    return render_template("index2.html")


@app.route("/orcamento", methods=["POST"])
def hello_world_2():
    return render_template("orcamento.html")

if __name__ == "__main__":
    app.run(debug=True)
