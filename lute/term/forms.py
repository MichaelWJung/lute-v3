"""
Flask-wtf forms.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, HiddenField, FieldList
from wtforms.validators import DataRequired


class TermForm(FlaskForm):
    """
    Term.
    """

    # TODO term form: add fields

    # TODO term form: language - use predefined
    language = SelectField(
        'Language',
        choices=[
            (1, 'English'),
        ])

    # TODO term form: hide this, change to HiddenField
    original_text = StringField('OriginalText')
    text = StringField('Text', validators=[DataRequired()], render_kw={"placeholder": "Term"})

    parents = FieldList(StringField('parent'))

    translation = StringField('Translation', render_kw={"placeholder": "Translation"})
    romanization = StringField('Romanization', render_kw={"placeholder": "Pronunciation"})
    status = StringField('Status', render_kw={"placeholder": "Status"})
    termtags = FieldList(StringField('termtag'))
    # TODO term form: hide this, change to HiddenField
    current_image = StringField('OriginalText')