"""
Language entity.
"""

import yaml
from lute.db import db


class Language(db.Model): # pylint: disable=too-few-public-methods
    """
    Language entity.
    """

    __tablename__ = 'languages'

    id = db.Column('LgID', db.SmallInteger, primary_key=True)
    name = db.Column('LgName', db.String(40))
    dict_1_uri = db.Column('LgDict1URI', db.String(200))
    dict_2_uri = db.Column('LgDict2URI', db.String(200))
    sentence_translate_uri = db.Column('LgGoogleTranslateURI', db.String(200))
    character_substitutions = db.Column(
        'LgCharacterSubstitutions', db.String(500),
        default="´='|`='|’='|‘='|...=…|..=‥")
    regexp_split_sentences = db.Column(
        'LgRegexpSplitSentences', db.String(500),
        default='.!?')
    exceptions_split_sentences = db.Column(
        'LgExceptionsSplitSentences', db.String(500),
        default='Mr.|Mrs.|Dr.|[A-Z].|Vd.|Vds.')
    word_characters = db.Column(
        'LgRegexpWordCharacters', db.String(500),
        default='a-zA-ZÀ-ÖØ-öø-ȳáéíóúÁÉÍÓÚñÑ')
    remove_spaces = db.Column('LgRemoveSpaces', db.Boolean, default=False)
    split_each_char = db.Column('LgSplitEachChar', db.Boolean, default=False)
    right_to_left = db.Column('LgRightToLeft', db.Boolean, default=False)
    show_romanization = db.Column('LgShowRomanization', db.Boolean, default=False)
    parser_type = db.Column('LgParserType', db.String(20), default='spacedel')

    def __repr__(self):
        return f"<Language {self.id} '{self.name}'>"


    @classmethod
    def fromYaml(cls, filename):
        """
        Create a new Language object from a yaml definition.
        """
        with open(filename, 'r') as file:
            d = yaml.safe_load(file)

        lang = cls()

        def load(key, method):
            if key in d:
                val = d[key]
                # Handle boolean values
                if isinstance(val, str):
                    temp = val.lower()
                    if temp == 'true':
                        val = True
                    elif temp == 'false':
                        val = False
                setattr(lang, method, val)

        # Define mappings for fields
        mappings = {
            'name': 'name',
            'dict_1': 'dict_1_uri',
            'dict_2': 'dict_2_uri',
            'sentence_translation': 'sentence_translate_uri',
            'show_romanization': 'show_romanization',
            'right_to_left': 'right_to_left',
            'parser_type': 'parser_type',
            'character_substitutions': 'character_substitutions',
            'split_sentences': 'regexp_split_sentences',
            'split_sentence_exceptions': 'exceptions_split_sentences',
            'word_chars': 'word_characters',
        }

        for key in d.keys():
            funcname = mappings.get(key, '')
            if funcname:
                load(key, funcname)

        return lang

    # relationships.
    # books = db.relationship('Book', backref='language', lazy='extra')
    # terms = db.relationship('Term', backref='language', lazy='extra')