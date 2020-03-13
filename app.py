from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html")
@app.route("/usuarios")
def usuarios():
    return render_template("users.html")
@app.route("/home")
def noticias():
    return render_template("home.html")
@app.route("/registro")
def registro():
    return render_template("form.html")