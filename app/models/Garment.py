from app import db

class Garment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    is_available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            brand = self.brand,
            size = self.size,
            color = self.color,
            condition = self.condition,
            price = self.price,
            description = self.description,
            is_available = self.is_available,
        )
    
    def create_instance_from_json(cls, json_data):
        return cls(
            title = json_data["title"],
            brand = json_data["brand"],
            size = json_data["size"],
            color = json_data["color"],
            condition = json_data["condition"],
            price = json_data["price"],
            description = json_data["description"],
        )