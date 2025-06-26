from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

@app.route('/')
def index():
    return {"message": "Welcome to the Late Show API!"}

if __name__ == '__main__':
    app.run(debug=True)