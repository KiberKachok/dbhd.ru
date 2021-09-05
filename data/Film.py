import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from kinopoisk.movie import Movie
from data import Film, Actor, db_session


class Film(SqlAlchemyBase):
    def __init__(self, kp_id, title, alt_title, about, year):
        self.kp_id = kp_id
        self.title = title
        self.alt_title = alt_title
        self.about = about
        self.year = year
        self.title_lower = self.title.lower()

    __tablename__ = 'films'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    kp_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    title_lower = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    alt_title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    actors = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)