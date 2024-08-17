from flask import Blueprint, flash, g, render_template, request, url_for, redirect
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
import flaskr.blogadmin

bp = Blueprint("blog", __name__)


@bp.route("/")
@login_required
def index():
    db, c = get_db()
    c.execute(
        "select * from user where user_id = %s",
        (g.user["user_id"],),
    )

    todos = c.fetchall()
    if todos is None:
        flash("No se pudo cargar el Usuario...")
    else:
        if g.user["admin"] == 1:
            return redirect(url_for("blogadmin.indexadmin"))
            #return render_template("blogadmin/index.html", todos=todos)
        if g.user["admin"] == 0:
            return render_template("blog/index.html", todos=todos)
        

    # return render_template("blog/index.html")
    #return render_template("blog/index.html", todos=todos)


@bp.route("/datospersonales", methods=["GET", "POST"])
@login_required
def datospersonales():
    db, c = get_db()
    c.execute(
        "select dp_id from datospersonales where dp_id = %s", (g.user["user_id"],)
    )

    if c.fetchone() is None:

        if request.method == "POST":
            sexo = request.form.get("sexo", False)
            edad = request.form.get("edad", False)
            escuelapreocedencia = request.form.get("escuelaprocedencia", False)
            foraneo = request.form.get("foraneo", False)
            trabajas = request.form.get("trabajas", False)
            becado = request.form.get("becado", False)
            discapacidad = request.form.get("discapacidad", False)

            error = None
            db, c = get_db()

            if not sexo:
                error = "Sexo requerido"
            if not edad:
                error = "Edad requerida"
            if not escuelapreocedencia:
                error = "Escuala de Procedencia es requerida"
            if not foraneo:
                error = "Foraneo es requerido"
            if not trabajas:
                error = "Trabajas es requerida"
            if not becado:
                error = "Becado es requerido"
            if not discapacidad:
                error = "Discapacidad es requerida"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into datospersonales (dp_id, sexo, edad, escuelaprocedencia, foraneo, trabajas, becado, discapacidad) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        sexo,
                        edad,
                        escuelapreocedencia,
                        foraneo,
                        trabajas,
                        becado,
                        discapacidad,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelsocioeconomico"))

            flash(error)

    else:
        return redirect(url_for("blog.nivelsocioeconomico"))

    return render_template("blog/datospersonales.html")


@bp.route("/nivelsocioeconomico", methods=["GET", "POST"])
@login_required
def nivelsocioeconomico():
    db, c = get_db()
    c.execute(
        "select ns_id from nivelsocioeconomico where ns_id = %s", (g.user["user_id"],)
    )

    if c.fetchone() is None:

        if request.method == "POST":
            nivelestudios = request.form.get("nivel_estudios_jg", False)
            numerobanos = request.form.get("numero_banos", False)
            numeroautos = request.form.get("numero_autos", False)
            internet = request.form.get("internet", False)
            numeropt = request.form.get("numero_pt", False)
            numerocd = request.form.get("numero_cd", False)

            error = None
            db, c = get_db()

            if not nivelestudios:
                error = "Nivel de Estudios requerido"
            if not numerobanos:
                error = "Numero de baños requerido"
            if not numeroautos:
                error = "Numero de Autos requerido"
            if not internet:
                error = "Disposicion de Internet requerido"
            if not numeropt:
                error = "Numero de personas que trabajas requerido"
            if not numerocd:
                error = "Numero de Cuartos para Dormir Requerido"
            if error is None:
                promedio = 1

                c.execute(
                    "insert into nivelsocioeconomico (ns_id, nivel_estudios_jh, numero_banos, numero_autos, internet, numero_pt, numero_cd, promedio) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        nivelestudios,
                        numerobanos,
                        numeroautos,
                        internet,
                        numeropt,
                        numerocd,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelmotivacional"))

            flash(error)
    else:
        return redirect(url_for("blog.nivelmotivacional"))

    return render_template("blog/nivelsocioeconomico.html")


@bp.route("/nivelmotivacional", methods=["GET", "POST"])
@login_required
def nivelmotivacional():
    db, c = get_db()
    c.execute(
        "select nm_id from nivelmotivacional where nm_id = %s", (g.user["user_id"],)
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)
            p6 = request.form["p6"]
            promedio += int(p6)
            p7 = request.form["p7"]
            promedio += int(p7)
            p8 = request.form["p8"]
            promedio += int(p8)
            p9 = request.form["p9"]
            promedio += int(p9)
            p10 = request.form["p10"]
            promedio += int(p10)

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"
            if not p6:
                error = "P6 requerido"
            if not p7:
                error = "P7 requerido"
            if not p8:
                error = "P8 requerido"
            if not p9:
                error = "P9 requerido"
            if not p10:
                error = "P10 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into nivelmotivacional (nm_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, promedio) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        p6,
                        p7,
                        p8,
                        p9,
                        p10,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelautoestima"))

            flash(error)
    else:
        return redirect(url_for("blog.nivelautoestima"))

    return render_template("blog/nivelmotivacional.html")


@bp.route("/nivelautoestima", methods=["GET", "POST"])
@login_required
def nivelautoestima():
    db, c = get_db()
    c.execute(
        "select na_id from nivelautoestima where na_id = %s", (g.user["user_id"],)
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)
            p6 = request.form["p6"]
            promedio += int(p6)
            p7 = request.form["p7"]
            promedio += int(p7)
            p8 = request.form["p8"]
            promedio += int(p8)
            p9 = request.form["p9"]
            promedio += int(p9)
            p10 = request.form["p10"]
            promedio += int(p10)

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"
            if not p6:
                error = "P6 requerido"
            if not p7:
                error = "P7 requerido"
            if not p8:
                error = "P8 requerido"
            if not p9:
                error = "P9 requerido"
            if not p10:
                error = "P10 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into nivelautoestima (na_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, promedio) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        p6,
                        p7,
                        p8,
                        p9,
                        p10,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelbienestarpsicologico"))

            flash(error)
    else:
        return redirect(url_for("blog.nivelbienestarpsicologico"))

    return render_template("blog/nivelautoestima.html")


@bp.route("/nivelbienestarpsicologico", methods=["GET", "POST"])
@login_required
def nivelbienestarpsicologico():
    db, c = get_db()
    c.execute(
        "select nbp_id from nivelbienestarpsicologico where nbp_id = %s",
        (g.user["user_id"],),
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)
            p6 = request.form["p6"]
            promedio += int(p6)
            p7 = request.form["p7"]
            promedio += int(p7)
            p8 = request.form["p8"]
            promedio += int(p8)
            p9 = request.form["p9"]
            promedio += int(p9)
            p10 = request.form["p10"]
            promedio += int(p10)

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"
            if not p6:
                error = "P6 requerido"
            if not p7:
                error = "P7 requerido"
            if not p8:
                error = "P8 requerido"
            if not p9:
                error = "P9 requerido"
            if not p10:
                error = "P10 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into nivelbienestarpsicologico (nbp_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, promedio) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        p6,
                        p7,
                        p8,
                        p9,
                        p10,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelhabitosestudio"))

            flash(error)
    else:
        return redirect(url_for("blog.nivelhabitosestudio"))

    return render_template("blog/nivelbienestarpsicologico.html")


@bp.route("/nivelhabitosestudio", methods=["GET", "POST"])
@login_required
def nivelhabitosestudio():
    db, c = get_db()
    c.execute(
        "select nhe_id from nivelhabitosestudio where nhe_id = %s", (g.user["user_id"],)
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)
            p6 = request.form["p6"]
            promedio += int(p6)
            p7 = request.form["p7"]
            promedio += int(p7)
            p8 = request.form["p8"]
            promedio += int(p8)
            p9 = request.form["p9"]
            promedio += int(p9)
            p10 = request.form["p10"]
            promedio += int(p10)

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"
            if not p6:
                error = "P6 requerido"
            if not p7:
                error = "P7 requerido"
            if not p8:
                error = "P8 requerido"
            if not p9:
                error = "P9 requerido"
            if not p10:
                error = "P10 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into nivelhabitosestudio (nhe_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, promedio) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        p6,
                        p7,
                        p8,
                        p9,
                        p10,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.nivelestrategiasaprendizaje"))

            flash(error)
    else:
        return redirect(url_for("blog.nivelestrategiasaprendizaje"))

    return render_template("blog/nivelhabitosestudio.html")


@bp.route("/nivelestrategiasaprendizaje", methods=["GET", "POST"])
@login_required
def nivelestrategiasaprendizaje():
    db, c = get_db()
    c.execute(
        "select nea_id from nivelestrategiasaprendizaje where nea_id = %s",
        (g.user["user_id"],),
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into nivelestrategiasaprendizaje (nea_id, p1, p2, p3, p4, p5, promedio) values (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.calidadinstitucion"))

            flash(error)
    else:
        return redirect(url_for("blog.calidadinstitucion"))

    return render_template("blog/nivelestrategiasaprendizaje.html")


@bp.route("/calidadinstitucion", methods=["GET", "POST"])
@login_required
def calidadinstitucion():
    db, c = get_db()
    c.execute(
        "select ci_id from calidadinstitucion where ci_id = %s",
        (g.user["user_id"],),
    )

    if c.fetchone() is None:
        if request.method == "POST":
            promedio = 0
            p1 = request.form["p1"]
            promedio += int(p1)
            p2 = request.form["p2"]
            promedio += int(p2)
            p3 = request.form["p3"]
            promedio += int(p3)
            p4 = request.form["p4"]
            promedio += int(p4)
            p5 = request.form["p5"]
            promedio += int(p5)
            p6 = request.form["p6"]

            db, c = get_db()
            error = None

            if not p1:
                error = "P1 requerido"
            if not p2:
                error = "P2 requerido"
            if not p3:
                error = "P3 requerido"
            if not p4:
                error = "P4 requerido"
            if not p5:
                error = "P5 requerido"
            if not p6:
                error = "p6 requerido"

            elif c.fetchone() is not None:
                error = "Usuario {} ya se encuentra evaluado.".format(
                    g.user["username"]
                )

            if error is None:
                c.execute(
                    "insert into calidadinstitucion (ci_id, p1, p2, p3, p4, p5, clase, promedio) values (%s, %s, %s, %s, %s, %s, %s,%s)",
                    (
                        g.user["user_id"],
                        p1,
                        p2,
                        p3,
                        p4,
                        p5,
                        p6,
                        promedio,
                    ),
                )
                db.commit()
                return redirect(url_for("blog.insertdatabase"))

            flash(error)
    else:
        return redirect(url_for("blog.insertdatabase"))

    return render_template("blog/calidadinstitucion.html")


def calcularpromedio(promedio):
    if promedio in range(1, 3):
        return 1
    if promedio in range(4, 7):
        return 2
    if promedio in range(8, 10):
        return 3


def calcularns(promedio):
    if promedio in range(0, 47):
        return 1
    if promedio in range(48, 94):
        return 2
    if promedio in range(95, 115):
        return 3
    if promedio in range(116, 140):
        return 4
    if promedio in range(141, 167):
        return 5
    if promedio in range(168, 201):
        return 6
    if promedio > 201:
        return 7


@bp.route("/insertdatabase")
@login_required
def insertdatabase():
    db, c = get_db()
    error = None
    c.execute(
        "select db_id from datab where db_id = %s",
        (g.user["user_id"],),
    )

    if c.fetchone() is None:
        sexo = dato("sexo", "datospersonales", "dp_id", g.user["user_id"])
        edad = dato("edad", "datospersonales", "dp_id", g.user["user_id"])
        ep = dato("escuelaprocedencia", "datospersonales", "dp_id", g.user["user_id"])
        foraneo = dato("foraneo", "datospersonales", "dp_id", g.user["user_id"])
        trabajas = dato("trabajas", "datospersonales", "dp_id", g.user["user_id"])
        becado = dato("becado", "datospersonales", "dp_id", g.user["user_id"])
        discapacidad = dato(
            "discapacidad", "datospersonales", "dp_id", g.user["user_id"]
        )
        ns = dato("promedio", "nivelsocioeconomico", "ns_id", g.user["user_id"])
        nm = dato("promedio", "nivelmotivacional", "nm_id", g.user["user_id"])
        na = dato("promedio", "nivelautoestima", "na_id", g.user["user_id"])
        nbp = dato("promedio", "nivelbienestarpsicologico", "nbp_id", g.user["user_id"])
        nhe = dato("promedio", "nivelhabitosestudio", "nhe_id", g.user["user_id"])
        nea = dato(
            "promedio", "nivelestrategiasaprendizaje", "nea_id", g.user["user_id"]
        )
        ci = dato("promedio", "calidadinstitucion", "ci_id", g.user["user_id"])
        clase = dato("clase", "calidadinstitucion", "ci_id", g.user["user_id"])

        if not sexo:
            error = "Sexo requerido"
        if not edad:
            error = "Edad requerido"
        if not ep:
            error = "Escuela de Procedencia requerido"
        if not foraneo:
            error = "Foraneo requerido"
        if not trabajas:
            error = "Trabajas requerido"
        if not becado:
            error = "Becado requerido"
        if not discapacidad:
            error = "Discapacidad requerido"
        if not ns:
            error = "Nivel socioeconomico requerido"
        if not nm:
            error = "Nivel Motivacional requerido"
        if not na:
            error = "Nivel Autoestima requerido"
        if not nbp:
            error = "Nivel Bienestar Psicologico requerido"
        if not nhe:
            error = "Nivel Habitos Estudios requerido"
        if not nea:
            error = "Nivel Estrategias de Apredizaje requerido"
        if not ci:
            error = "Calida de Institucion requerido"

        if error is None:
            c.execute(
                "insert into datab (db_id, sexo, edad, escuelaprocedencia, foraneo, trabajas, becado, discapacidad, ns, nm, na, nbp, nhe, nea, ci, clase) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    g.user["user_id"],
                    sexo["sexo"],
                    edad["edad"],
                    ep["escuelaprocedencia"],
                    foraneo["foraneo"],
                    trabajas["trabajas"],
                    becado["becado"],
                    discapacidad["discapacidad"],
                    ns["promedio"],
                    nm["promedio"],
                    na["promedio"],
                    nbp["promedio"],
                    nhe["promedio"],
                    nea["promedio"],
                    ci["promedio"],
                    clase["clase"],
                ),
            )
            db.commit()
            flash("Datos registrados correctamente...")

            return redirect(url_for("blog.index"))

    else:
        flash("Ya realizaste la Autoevaluacion")
        return redirect(url_for("blog.index"))

    return redirect(url_for("blog.index"))


def dato(dato, tabla, id_columna, id_valor):
    db, c = get_db()
    c.execute(f"SELECT {dato} FROM {tabla} WHERE {id_columna} = {id_valor}")
    dato_obtenido = c.fetchone()
    if dato_obtenido is not None:
        return dato_obtenido
    else:
        return 1


@bp.route("/evaluaciondocente", methods=["GET", "POST"])
@login_required
def evaluaciondocente():
    

    return render_template("blog/evaluaciondocente.html")
