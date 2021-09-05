from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search_request = StringField('Название', validators=[DataRequired()],
                                 render_kw={"placeholder": "Название фильма или имя актёра",
                                            "style": "height: 26px; font-size: 12pt;"})
    submit = SubmitField('Искать')
