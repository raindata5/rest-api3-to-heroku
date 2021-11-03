from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.languagefamily import LanguageFamilyModel


class LanguageFamily(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument(arg, help=str, required=bool, type=str)

    def get(self, name):
        row = LanguageFamilyModel.get_row_by_name(name)
        if row:
            return row.json()
        return {'message': 'language family not found'}, 404

    def post(self, name):
        if LanguageFamilyModel.get_row_by_name(name):
            return {'message': '{0} already exists'.format(name)}, 400
        new_language_family_model = LanguageFamilyModel(name)
        try:
            new_language_family_model.save_to_database()
        except Exception:
            return {'message': 'an error occurred with inserting the language family'}, 500

        return new_language_family_model.json(), 201


    def delete(self, name):
        lf = LanguageFamilyModel.get_row_by_name(name)
        if lf:
            lf.del_from_database()

        return {'message': 'lang family no longer in db'}




class LanguageFamilyList(Resource):
    def get(self):
        return {'language family': [lf.json() for lf in LanguageFamilyModel.query.all()]}
