from flask import Flask, render_template, request, flash
from database import create_db,getDB
from models.contact import Contact
from models.address import Address
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/contact"
app.config["FLASK_ENV"] = "development"
app.secret_key = 'thesecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
create_db(app)
db = getDB()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    flash('this is a flashed message')
    return render_template("home.html")

@app.route("/save", methods=["POST"])
def save():
    return 'saved!'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


