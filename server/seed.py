from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask import Flask
from datetime import date
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Emma Stone", occupation="Actress")
    g2 = Guest(name="Trevor Noah", occupation="Comedian")
    e1 = Episode(date=date(2024, 5, 20), number=101)
    e2 = Episode(date=date(2024, 6, 5), number=102)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()

    a1 = Appearance(rating=4, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=5, guest_id=g2.id, episode_id=e2.id)

    db.session.add_all([a1, a2])
    db.session.commit()

    print(" Database seeded successfully.")
