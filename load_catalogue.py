from models import Meal, Option, db_session
from catalogue import catalogue


def update_db(catalogue):
    for meal in catalogue:
        meal_to_add = Meal(title=meal["title"],
                            description=meal["description"])
        for choice in meal["choices"]:
            option = Option(size=choice["title"], price=choice["price"])
            meal_to_add.options.append(option)
        db_session.add(meal_to_add)
    db_session.commit()


if __name__ == '__main__':
    update_db(catalogue)
