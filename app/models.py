from app import db

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    iso_code = db.Column(db.String(5), unique=True)
    divisions = db.relationship('AdministrativeDivision', backref='country', lazy=True)

class AdministrativeDivision(db.Model):
    __tablename__ = 'administrative_divisions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer) 
    
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('administrative_divisions.id'), nullable=True)
    
    sub_divisions = db.relationship('AdministrativeDivision', 
                                    backref=db.backref('parent', remote_side=[id]),
                                    lazy=True)