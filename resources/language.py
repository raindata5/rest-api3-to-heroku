from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.language import LanguageModel

class Language(Resource):

    parser = reqparse.RequestParser()  # what does this data do?
    parser.add_argument('country', help='This country needs to be a string and is a required field', required=False, type=str)
    parser.add_argument('language_family_id', help='This language needs a language_family_id', required=True, type=str)

    @jwt_required()  # why is this placed here?
    def get(self, name):
        row = LanguageModel.get_row_by_name(name)
        if row:
            # return {'language': {'name': name, 'country': row[1]}}
            return row.json()
        return {'message': 'language isn\'t present'}, 400


    def post(self, name):

        if LanguageModel.get_row_by_name(name):
            return {'message': '{0} already exists'.format(name)}, 400

        # why place this line in this particular spot?
        data = Language.parser.parse_args()
        language = LanguageModel(name, data['country'], data['language_family_id'])
        try:
            language.save_to_database()
        except Exception:
            return {'message': 'an error occurred with inserting the language'}, 500

        return language.json(), 201



    def delete(self, name):
        language = LanguageModel.get_row_by_name(name)
        if language:
            language.del_from_database()

        return {'message': 'Language deleted'}


    def put(self, name):
        language = LanguageModel.get_row_by_name(name)
        data = Language.parser.parse_args()

        if language:
            try:
                language.country = data['country']
                language.language_family_id = data['language_family_id']
            except Exception:
                return {'message': 'an error occurred with updating the language'}, 500
        else:
            try:
                language = LanguageModel(name, **data)
            except Exception:
                return {'message': 'an error occurred with inserting the language'}, 500
        language.save_to_database()
        return language.json()


class LanguageList(Resource):

    def get(self):

        return {'languages': [language.json() for language in LanguageModel.query.all()]}
        # alternative is
        # list(map(lambda x: x.json(), LanguageModel.query.all()))
