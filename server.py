from flask import Flask, render_template
from flask_admin import Admin
from models import Meal, Option, db_session
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)


admin = Admin(app, name='Pizzashop', template_mode='bootstrap3')
admin.add_view(ModelView(Meal, db_session))
admin.add_view(ModelView(Option, db_session))


if __name__ == '__main__':
    app.run()