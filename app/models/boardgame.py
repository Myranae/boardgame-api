from app import db

class Boardgame(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    creator = db.Column(db.String)
    length = db.Column(db.Integer)
    producer = db.Column(db.String)
    genre = db.Column(db.String)

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            creator = self.creator,
            length = self.length,
            producer = self.producer,
            genre = self.genre,
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            # creator=data_dict["creator"],
            # length=data_dict["length"],
            # producer=data_dict["producer"],
            # genre=data_dict["genre"],
        )