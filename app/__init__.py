from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    CORS(app)
    Swagger(app)

    from app.routes.invocations import invocations_bp
    app.register_blueprint(invocations_bp, url_prefix="/api/invocations")

    with app.app_context():
        from app.utils.seed import seed_data
        from app.models import Invocation
        db.create_all()
        seed_data()

    return app