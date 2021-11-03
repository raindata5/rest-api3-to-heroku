import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity  # using JWT to make call to these formulas
from resources.user import UserRegister
from resources.language import Language, LanguageList
# from sqlalc import db
from resources.languagefamily import LanguageFamilyList, LanguageFamily

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///flask-languages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'burbuja'

api = Api(app)


# @app.before_first_request  # why?
# def create_tables():
#     db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(LanguageFamilyList, '/languagefamilies')
api.add_resource(LanguageFamily, '/languagefamily/<string:name>')
api.add_resource(Language, '/language/<string:name>')
api.add_resource(LanguageList, '/languages')
api.add_resource(UserRegister, '/registration')


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
