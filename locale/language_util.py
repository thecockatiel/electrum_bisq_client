import babel

class LanguageUtil:
    @staticmethod
    def get_default_language():
        return babel.parse_locale(babel.default_locale())[0]