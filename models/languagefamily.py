from sqlalc import db

class LanguageFamilyModel(db.Model):

    __tablename__ = 'Language_Family'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))

    languages = db.relationship('LanguageModel', lazy='dynamic')  # why do we have dynamic here

    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'languages': [language.json() for language in self.languages.all()]}


    @classmethod
    def get_row_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def save_to_database(self):  # why name as such?
        db.session.add(self)
        db.session.commit()


    def del_from_database(self):
        db.session.delete(self)
        db.session.commit()
