import os
import argparse
import json
from models import Meal, Option, db_session
from catalogue import catalogue


def update_db(data):
    for item in data:
        first_option_to_add = Option(size=item["choices"][0]["title"], price=item["choices"][0]["price"])
        db_session.add(first_option_to_add)
        second_option_to_add = Option(size=item["choices"][1]["title"], price=item["choices"][1]["price"])
        db_session.add(second_option_to_add)
        db_session.flush()
        meal_to_add = Meal(title=item["title"], description=item["description"], first_option_id=first_option_to_add.id, second_option_id=second_option_to_add.id)
        db_session.add(meal_to_add)
    db_session.commit()


if __name__ == '__main__':
    update_db(catalogue)
