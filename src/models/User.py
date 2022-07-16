from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    ## tables definitions here
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    age = db.Column(db.String(120))
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'age': self.age,
        }