import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.Garment import Garment


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_garments(app):
    # Arrange
    garment1 = Garment(
        title="Arabella Gown",
        brand="BHLDN",
        size=8,
        color="ivory",
        condition="Excellent used condition",
        price="800",
        description="A beautiful, flowy blush gown"
    )

    garment2 = Garment(
        title="Lenox Short Suit",
        brand="Christian Siriano",
        size=16,
        color="black",
        condition="New with tags",
        price="400",
        description="A fresh, modern take on the courthouse wedding suit"
    )

    db.session.add_all([garment1, garment2])
    db.session.commit()