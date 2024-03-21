from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Ninja.get_one_dojo_with_ninjas(data)
    print("Datos del dojo", dojo)
    return render_template('dojo_show.html',dojo = dojo)
