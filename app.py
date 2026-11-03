from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import db
import hashlib
import filetype
from werkzeug.utils import secure_filename
import hashlib, filetype, os, random, uuid
from datetime import datetime, timedelta
import time
from flask_cors import cross_origin


UPLOAD_FOLDER = 'static/uploads' #Guardamos cosas

app = Flask(__name__) #creamos la app
app.secret_key = "s3cr3t_k3y"#Para darle una idea particular a la aplicación que estamos trabajando
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #La aplicación sabe cuál es el update folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/")
def index():
    db_session = db.Sessionlocal()
    avistamientos = db_session.query(db.Avistamiento).order_by(db.Avistamiento.fecha_hora.desc()).limit(2).all()
    db_session.close()
    return render_template("portada.html", avistamientos=avistamientos)

@app.route("/register", methods=["GET", "POST"]) #get para cambiar el registro y post para mandar un resgistro
def register():
#Lo vinculamos a la db de regiones
    db_session = db.Sessionlocal()
    regiones = db_session.query(db.Region).all()
    region_id = request.form.get("region-voluntario")
    if region_id:
        comunas = db_session.query(db.Comuna).filter(db.Comuna.region_id == int(region_id)).all()
    else:
        comunas = []

    if request.method == "POST":
        #comunas por región
        if not request.form.get("nombre-voluntario") and not request.form.get("correo-voluntario"):
            db_session.close()
            return render_template(
                "registro.html",
                regiones=regiones,
                comunas=comunas,
                region_id=region_id
            )
        nombre = request.form.get("nombre-voluntario")
        email = request.form.get("correo-voluntario")
        comuna = request.form.get("comuna-voluntario")
        if not nombre:
            return render_template("registro.html", error="Ingrese su nombre", regiones=regiones, comunas=comunas, region_id=region_id)
        if not email:
            return render_template("registro.html", error="Ingrese email válido", regiones=regiones, comunas=comunas, region_id=region_id)
        if not comuna:
            return render_template("registro.html", error="Ingrese una comuna", regiones=regiones, comunas=comunas, region_id=region_id)

        voluntario = db.Voluntario(nombre=nombre, email=email, comuna_id=comuna)
        db_session.add(voluntario)
        db_session.commit()
        db_session.close()

        return "Registro recibido"

    
    db_session.close()
    return render_template("registro.html", regiones=regiones, comunas=comunas, region_id=region_id)

@app.route("/avistamientos", methods=["GET", "POST"])
def avistamiento():
    return render_template("avistamiento.html")

@app.route("/stats", methods=["GET", "POST"])
def stats():
    return render_template("stats.html")

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_stats_data():
    #como no tenemos avistamientos todavía vamos a crear unos para ver como se ven (ver como se ven xd)
    get_fecha_random = lambda start_date, end_date : start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds)))
    get_random_int = lambda start_int, end_int: random.randint(start_int, end_int)
    
    random_data = [{
        "date": get_fecha_random(datetime(2023, 1, 1), datetime(2026, 10, 31)),
        "count": get_random_int(1, 10)
    } for _ in range(50)]
    random_data.sort(key=lambda x: x["date"])
    
    for row in random_data:
            row["date"] = row["date"].strftime("%Y-%m-%d")
    time.sleep(5)
    return jsonify(random_data)

if __name__ == "__main__":
    app.run(debug=True)