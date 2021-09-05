import sqlalchemy
from data import db_session, Hash


def is_moderator(hash) -> bool:
    session = db_session.create_session()
    mod = session.query(Hash.Hash).filter(Hash.Hash.hashcode == hash).first()

    if mod:
        return True
    else:
        return False
