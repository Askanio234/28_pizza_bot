from flask import Flask, render_template
from models import Meal, Option, db_session


app = Flask(__name__)

@app.route('/admin')
def load_admin():
    query = db_session.query(Meal).all()
    return render_template('admin.html', meals=query)

if __name__ == '__main__':
    app.run()