#!/usr/bin/env python
from app import db
db.create_all()

from models import Tick
franio = Tick(longitude=52.2297, latitude=21.0122, is_test=True, sex=False, age=18, date='2019-03-24')
zenek = Tick(longitude=51.5074, latitude=0.1278, is_test=True, sex=False, age=17, date='2019-03-24')

db.session.add_all([franio, zenek])
db.session.commit()
