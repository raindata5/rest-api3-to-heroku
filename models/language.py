from sqlalc import db

class LanguageModel(db.Model):

    __tablename__ = 'Language'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    country = db.Column(db.String(40))
    language_family_id = db.Column(db.Integer, db.ForeignKey('Language_Family.id'))

    language_family = db.relationship('LanguageFamilyModel')
    def __init__(self, name, country, language_family_id):
        self.name = name
        self.country = country
        self.language_family_id = language_family_id

    def json(self):
        return {'name': self.name, 'country': self.country}


    @classmethod
    def get_row_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def save_to_database(self):  # why name as such?
        db.session.add(self)
        db.session.commit()


    def del_from_database(self):
        db.session.delete(self)
        db.session.commit()
