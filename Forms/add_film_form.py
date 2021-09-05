from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class AddFilmForm(FlaskForm):
    kp_id = StringField('Название', validators=[DataRequired()], render_kw={"placeholder": "КиноПоиск id"})
    # moderator_hash = StringField('moderator_hash', validators=[DataRequired()], render_kw={"placeholder": "moderator_hash"})
    submit = SubmitField('готово')


