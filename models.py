from app import app, db
import datetime as dt

class Tick(db.Model):

    def __init__(self, **kwargs):

        if not isinstance(kwargs['date'], dt.datetime):
            date = dt.datetime.strptime(kwargs['date'], '%Y-%m-%d')
            print(type(date))
            kwargs['date'] = date

        super().__init__(**kwargs)
        print(kwargs['date'])

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float(), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    is_test = db.Column(db.Boolean(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    # disease = db.Column(db.String(100))
    sex = db.Column(db.Boolean(), nullable=False)
    age = db.Column(db.Integer, nullable=True)


    def czy_jest_starszy_niz(self, n_lat):
        return self.age > n_lat

    @property
    def sex_name(self):
        return 'female' if self.sex else 'male'
    # male = True, female = False

    def __repr__(self):
        return '<Tick %r>' % self.id

    def to_dict(self):


        tick = {'id': self.id,
                'longitude': self.longitude,
                'latitude': self.latitude,
                'is_test': self.is_test,
                'date': str(self.date),
                'sex': self.sex_name,
                'age': self.age
                }

        return tick

