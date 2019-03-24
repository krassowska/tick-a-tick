from app import app, db


class Tick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float(), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    is_test = db.Column(db.Boolean(), nullable=False)
    # date_of_bite = db.Column(db.Date(), nullable=False)
    # disease = db.Column(db.String(100))
    sex = db.Column(db.Boolean(), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Tick %r>' % self.id

