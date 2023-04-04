from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/contact"
app.config["FLASK_ENV"] = "development"
app.secret_key = 'thesecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

from enum import Enum
class degree(Enum):
    associate = 0
    bachelor = 1
    master = 1 
    doctoral = 1
    professional = 1


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    national_id = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Boolean)
    gpa = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=sqlalchemy.sql.func.now())
    birthday = db.Column(db.DateTime(timezone=True),nullable = True)
    description = db.Column(db.Text(1000), nullable=True, primary_key=False)
    degree = db.Column(sqlalchemy.Enum(degree), nullable=True, primary_key=False)
    def __repr__(self):
        return "<NationalId: {}>".format(self.first_name + " " + self.last_name)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    flash('this is a flashed message')
    return render_template("home.html")

@app.route("/save", methods=["POST"])
def save():
    return 'saved!'

@app.route("/migrate", methods=["GET"])
def migrate():
    Migrate(app,db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


