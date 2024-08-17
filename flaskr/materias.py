from flask import Blueprint, app, flash, g, render_template, request, url_for, redirect
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash
from flaskr.auth import login_required
from flaskr.db import get_db
import pandas as pd

bp = Blueprint("materias", __name__)

@bp.route("/materias")
@login_required
def materias():
    db, c = get_db()
    '''c.execute(
        "select * from user where user_id = %s",
        (g.user["user_id"],),
    )

    todos = c.fetchall()'''
    c.execute(
        "SELECT inscripcion_id, nombre, materias.materias_id FROM inscripcion JOIN materias ON materias.materias_id = inscripcion.materias_id where alumno_id = %s",(g.user["user_id"],),
    )
    todos = c.fetchall()
    # return render_template("blog/index.html")
    return render_template("materias/materias.html", todos=todos)

@bp.route('/evaluaciondocente/<int:inscripcion_id>/<string:nombre>/<int:materia_id>', methods=["GET", "POST"])
@login_required
def evaluaciondocente(inscripcion_id, nombre, materia_id):
    db, c= get_db()
        
    c.execute(
        "SELECT inscripcion_id from evaluacion where inscripcion_id = %s", (inscripcion_id,),
    )
    if c.fetchone() is None:
        if request.method == "POST":
            EA = request.form["p1"]
            RA = request.form["p2"]
            UM = request.form["p3"]
            FD = request.form["p4"]
            comentario = request.form["comentario"]
            c.execute(
                "INSERT INTO evaluacion(inscripcion_id, valor1, valor2, valor3, valor4) VALUES(%s, %s, %s, %s, %s)",
                (inscripcion_id, EA, RA, UM, FD),
            )
            
            db.commit()
            flash("Materia Evaluada Correctamente...")
            return redirect(url_for("materias.materias"))
    else:
        flash("Materia ya evaluada...")
        return redirect(url_for("materias.materias"))
    
    return render_template('materias/evaluaciondocente.html', nombre=nombre)
