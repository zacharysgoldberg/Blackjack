import os
from sqlalchemy import create_engine


def create_db():
    engine = create_engine('sqlite:///app/api/db/blackjack.db', echo=True)
    return engine
