import os
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
    meal_id = Column(Integer, primary_key=True)
    options = relationship("Option", backref="option")
    title = Column(String(50))
    description = Column(String(200))

    def __str__(self):
        return "{} с {}".format(self.title, self.description)


class Option(data_base):
    __tablename__ = "meal_option"
    option_id = Column(Integer, primary_key=True)
    price = Column(Integer)
    size = Column(String(100))
    meal_id = Column(Integer, ForeignKey("meals.meal_id"))

    def __str__(self):
        return "{} за {}р.".format(self.size, self.price)


if __name__ == '__main__':
    data_base.metadata.drop_all(bind=engine)
    data_base.metadata.create_all(bind=engine)
