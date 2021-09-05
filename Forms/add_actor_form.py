from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class AddActorForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()], render_kw={"placeholder": "Имя"})
    about = TextAreaField('Описание', render_kw={"placeholder": "Описание", "rows": "5"})
    # moderator_hash = StringField('moderator_hash', validators=[DataRequired()], render_kw={"placeholder": "moderator_hash"})
    submit = SubmitField('готово')
