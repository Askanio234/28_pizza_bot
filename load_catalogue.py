import os
import argparse
import json
from models import Meal, Option, db_session
from catalogue import catalogue


def update_db(data):
    for item in data:
        meal = Meal(title=item["title"], description=item["description"])
        for choice in item["choices"]:
            option = Option(size=choice["title"], price=choice["price"])
            meal.options.append(option)
        db_session.add(meal)
    db_session.commit()


if __name__ == '__main__':
    update_db(catalogue)
