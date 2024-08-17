import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE=os.environ.get("FLASK_DATABASE"),
    )
    
    
    from . import db
    
    db.init_app(app)
    
    from . import auth 
    from . import blog
    from . import blogadmin
    from . import materias

    
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(blogadmin.bp)
    app.register_blueprint(materias.bp)

    @app.route("/hola")
    def hola():
        return "hola"

    return app
