import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Hash(SqlAlchemyBase):
    def __init__(self, name, about):
        self.name = name
        self.about = about

    __tablename__ = 'hashs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashcode = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)