from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from app import create_db


db = create_db()

Base = declarative_base()

# [users table]


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    username = Column(String(128), nullable=False,
                      unique=True, index=True)
    password = Column(String(128), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    leaderboard_id = Column(Integer, ForeignKey('leaderboard.id'))


# [leaderboard table]


class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(200), nullable=False, index=True)
    wins = Column(BigInteger, nullable=True)
    losses = Column(BigInteger, nullable=True)
    last_game = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=True)

    user = relationship(
        'User', backref='leaderboard', uselist=False)


Base.metadata.create_all(db)

Session = sessionmaker(bind=db)

session = Session()
