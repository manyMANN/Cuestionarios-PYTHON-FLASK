import functools
from flask import (
    Blueprint,
    flash,
    g,
    render_template,
    request,
    redirect,
    url_for,
    session,
)
from werkzeug.security import check_password_hash, generate_password_hash
#from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_id = request.form["user_id"]
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        bloque = request.form["bloque"]
        preparatoria = request.form["preparatoria"]
        seccion = request.form["seccion"]
        semestre = request.form["semestre"]

        db, c = get_db()
        error = None
        c.execute("select user_id from user where user_id = %s", (user_id,))
        if not user_id:
            error = "User id es requerido"
        if not email:
            error = "Email id es requerido"
        if not password:
            error = "Password es requerido"
        if not username:
            error = "Username id es requerido"
        if not bloque:
            error = "Bloque id es requerido"
        if not preparatoria:
            error = "Preparatoria id es requerido"
        if not seccion:
            error = "Seccion id es requerido"
        if not semestre:
            error = "Semestre id es requerido"

        elif c.fetchone() is not None:
            error = "Usuario {} se encuentra registrado.".format(user_id)

        if error is None:
            c.execute(
                "insert into user (user_id, email, password, username, bloque, preparatoria, seccion, semestre) values (%s, %s, %s, %s, %s, %s, %s,%s)",
                (
                    user_id,
                    email,
                    generate_password_hash(password),
                    username,
                    bloque,
                    preparatoria,
                    seccion,
                    semestre,
                ),
            )
            registrarAlumno(user_id, username, semestre)
            db.commit()
            
            return redirect(url_for("blogadmin.indexadmin"))
            #return redirect(url_for("auth.inscribirmaterias", user_id=user_id, username=username, semestre=semestre))

        flash(error)

    return render_template("auth/registeruser.html")
      
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

@bp.route("/registeradmin", methods=["GET", "POST"])
def registeradmin():
    if request.method == "POST":
        user_id = request.form["user_id"]
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        institucion = request.form["institucion"]

        db, c = get_db()
        error = None
        c.execute("select user_id from user where user_id = %s", (user_id,))
        if not user_id:
            error = "User id es requerido"
        if not email:
            error = "Email id es requerido"
        if not password:
            error = "Password es requerido"
        if not username:
            error = "Username id es requerido"
        if not institucion:
            error = "Institucion id es requerido"
        

        elif c.fetchone() is not None:
            error = "Usuario {} se encuentra registrado.".format(user_id)

        if error is None:
            c.execute(
                "insert into user (user_id, email, password, username, bloque, preparatoria, seccion, semestre, admin) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    user_id,
                    email,
                    generate_password_hash(password),
                    username,
                    "",
                    institucion,
                    "",
                    0,
                    1,
                ),
            )

            db.commit()

            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("authadmin/registeradmin.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        db, c = get_db()
        error = None

        c.execute("select * from user where email = %s", (email,))
        user = c.fetchone()
        if user is None:
            error = "Usuario y/o Contraseña invalida..."
        elif not check_password_hash(user["password"], password):
            error = "Usuario y/o Contraseña invalida..."
        if error is None:
            session.clear()
            session["user_id"] = user["user_id"]
            return redirect(url_for("blog.index"))

        flash(error)
    return render_template("auth/loginuser.html")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute("select * from user where user_id = %s", (user_id,))
        g.user = c.fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
