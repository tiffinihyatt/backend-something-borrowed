from app import db

class Garment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    street_size = db.Column(db.Integer, nullable=False)
    label_size = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String)
    is_available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            brand = self.brand,
            street_size = self.street_size,
            label_size = self.label_size,
            color = self.color,
            condition = self.condition,
            price = self.price,
            description = self.description,
            is_available = self.is_available,
        )