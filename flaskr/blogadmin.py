from flask import Blueprint, app, flash, g, render_template, request, url_for, redirect
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash
from flaskr.auth import login_required
from flaskr.db import get_db
import pandas as pd

bp = Blueprint("blogadmin", __name__)


@bp.route("/indexadmin")
@login_required
def indexadmin():
    db, c = get_db()
    c.execute(
        "select * from user where user_id = %s",
        (g.user["user_id"],),
    )

    todos = c.fetchall()
    # return render_template("blog/index.html")
    return render_template("blogadmin/index.html", todos=todos)

@bp.route("/registraralumnos", methods=["GET", "POST"])
@login_required
def registraralumnos():
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        
        df = pd.read_excel(file)
        db, c = get_db()
        error = None
        for index, row in df.iterrows():
            id = int(row['MATRÍCULA'])
            c.execute("select user_id from user where user_id = %s", (id,),)
            if c.fetchone() is None:
                password = str(row["MATRÍCULA"])
                user_id = row['MATRÍCULA']
                username = row['NOMBRE']
                semestre = row['SEMESTRE']
                
                c.execute("INSERT INTO user (user_id, email, password, username, bloque, preparatoria, seccion, semestre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                            (row['MATRÍCULA'], row['EMAIL_INST'], generate_password_hash(password), row['NOMBRE'], row['BLOQUE'], row['PREPARATORIA'], row['SECCIÓN'],row['SEMESTRE'],),)
                
                db.commit()
                registrarAlumno(user_id, username, semestre)
                flash("Usuarios registrados exitosamente...")
            else:
                flash("Usuario {} se encuentra registrado.".format(row['MATRÍCULA']))
        
        return redirect(url_for("blogadmin.indexadmin"))

        
    return render_template("blogadmin/registraralumnos.html")

def registrarAlumno(user_id, username,semestre):
    db, c = get_db()
    c.execute("select alumno_id from alumno where alumno_id = %s", (user_id,),)
    result = c.fetchone()
    if result is None:
        c.execute(
            "insert into alumno(alumno_id, username, semestre) values (%s, %s, %s)", (user_id, username, semestre),
        )
        inscribirmaterias2(user_id, semestre)
        db.commit()
        
def inscribirmaterias2(user_id, semestre):
    semestrec = int(semestre)
    db, c = get_db()
    
    materias_por_semestre = {
        1: [1, 2, 3, 4, 5, 6, 7, 8],
        2: [9, 10, 11, 12, 13, 14, 15, 16],
        3: [17, 18, 19, 20, 21, 22],
        4: [23, 24, 25, 26, 27, 28],
        5: [29, 30, 31, 32, 33, 34],
        6: [35, 36, 37, 38, 39, 40]
    }
        
    for materia_id in materias_por_semestre.get(semestrec, []):
        c.execute(
            "INSERT INTO inscripcion(alumno_id, materias_id, semestre_id) VALUES (%s, %s, %s)",
            (user_id, materia_id, semestre)
        )

        db.commit()
        
    flash("Datos registrados correctamente...")
    return redirect(url_for("blogadmin.indexadmin"))

@bp.route("/registraradministradores", methods=["GET", "POST"])
@login_required
def registraradministradores():
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        
        df = pd.read_excel(file)
        db, c = get_db()
        error = None
        for index, row in df.iterrows():
            id = int(row['MATRÍCULA'])
            c.execute("select user_id from user where user_id = %s", (id,),)
            if c.fetchone() is None:
                password = str(row["MATRÍCULA"])
                c.execute("INSERT INTO user (user_id, email, password, username, bloque, preparatoria, seccion, admin) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", 
                            (row['MATRÍCULA'], row['EMAIL_INST'], generate_password_hash(password), row['NOMBRE'], "", row['PREPARATORIA'], "", 1,),)
                db.commit()
                flash("Administrador registrados exitosamente...")
            else:
                flash("Administrador {} se encuentra registrado.".format(row['MATRÍCULA']))
        
        return redirect(url_for("blogadmin.indexadmin"))
    
        
    return render_template("blogadmin/registraradministradores.html")