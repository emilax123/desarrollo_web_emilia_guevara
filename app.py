from flask import Flask, request, render_template, redirect, url_for, session
import db
import hashlib
import filetype

UPLOAD_FOLDER = 'static/uploads' #Guardamos cosas

app = Flask(__name__) #creamos la app
app.secret_key = "s3cr3t_k3y"#Para darle una idea particular a la aplicación que estamos trabajando
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #La aplicación sabe cuál es el update folder

@app.route("/")
def index():
    db_session = db.Sessionlocal()
    avistamientos = db_session.query(db.Avistamiento).order_by(db.Avistamiento.fecha_hora.desc()).limit(2).all()
    db_session.close()
    return render_template("portada.html", avistamientos=avistamientos)

@app.route("/register", methods=["GET", "POST"]) #get para cambiar el registro y post para mandar un resgistro
@app.route("/register", methods=["GET", "POST"])
def register():
    db_session = db.Sessionlocal()

    regiones = db_session.query(db.Region).all()

    region_id = request.args.get("region")

    if region_id:
        comunas = db_session.query(db.Comuna).filter(
            db.Comuna.region_id == int(region_id)
        ).all()
    else:
        comunas = []

    if request.method == "POST":
        nombre = request.form.get("nombre-voluntario")
        email = request.form.get("correo-voluntario")
        comuna = request.form.get("comuna-voluntario")

        if not nombre or not email or not comuna:
            db_session.close()
            return render_template(
                "registro.html",
                regiones=regiones,
                comunas=comunas,
                region_id=region_id
            )

        voluntario = db.Voluntario(
            nombre=nombre,
            email=email,
            comuna_id=comuna
        )

        db_session.add(voluntario)
        db_session.commit()
        db_session.close()

        return "Registro recibido"

    db_session.close()

    return render_template(
        "registro.html",
        regiones=regiones,
        comunas=comunas,
        region_id=region_id
    )

@app.route("/avistamientos", methods=["GET", "POST"])
def avistamiento():
    return render_template("avistamiento.html")


if __name__ == "__main__":
    app.run(debug=True)