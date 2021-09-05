import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Actor(SqlAlchemyBase):
    def __init__(self, name):
        self.name = name
        self.name_lower = name.lower()

    __tablename__ = 'actors'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    name_lower = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    films = sqlalchemy.Column(sqlalchemy.Integer)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)