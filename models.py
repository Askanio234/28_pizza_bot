import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


databse_uri = os.getenv("db_uri", "sqlite:///pizza_shop.sqlite")

engine = create_engine(databse_uri)

db_session = scoped_session(sessionmaker(bind=engine))

data_base = declarative_base()

data_base.query = db_session.query_property()


class Meal(data_base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    first_option_id = Column(Integer, ForeignKey("meal_option.id"))
    second_option_id = Column(Integer, ForeignKey("meal_option.id"))
    first_option = relationship("Option", foreign_keys=[first_option_id])
    second_option = relationship("Option", foreign_keys=[second_option_id])
    title = Column(String(50))
    description = Column(String(200))

    def __str__(self):
        return "{} with {}".format(self.title, self.description)


class Option(data_base):
    __tablename__ = "meal_option"
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    size = Column(String(100))

    def __str__(self):
        return "a {} option at {}".format(self.size, self.price)


if __name__ == '__main__':
    data_base.metadata.drop_all(bind=engine)
    data_base.metadata.create_all(bind=engine)