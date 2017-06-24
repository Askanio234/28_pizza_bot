import os
from functools import wraps
from flask import Flask, render_template, request, Response
from flask_admin import Admin
from models import Meal, Option, db_session
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('secret_key')


class AuthException(HTTPException):

    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class MyModelView(ModelView):

    def check_auth(self, username, password):
        return username == os.getenv('username') and password == os.getenv('password')

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


admin = Admin(app, name='Pizzashop', template_mode='bootstrap3')
admin.add_view(MyModelView(Meal, db_session))
admin.add_view(MyModelView(Option, db_session))



if __name__ == '__main__':
    app.run()