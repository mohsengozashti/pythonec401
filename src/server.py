from flask import Flask, render_template, request, flash,redirect,url_for,abort
from database import create_db,getDB
from models.contact import Contact,Degree
from models.address import Address
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/contact"
app.config["FLASK_ENV"] = "development"
app.secret_key = 'thesecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
create_db(app)
db = getDB()




@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        addresses = {}
        # Loop through all items in the form data
        for key, value in request.form.items():
            if key.startswith('address'):
                # Split the key to get the address number and attribute name
                parts = key.split('[')
                address_num = parts[1].rstrip(']')
                attribute_name = parts[2].rstrip(']')
            
                # Create a dictionary for the address if it doesn't exist yet
                if address_num not in addresses:
                    addresses[address_num] = {}
            
                # Add the attribute to the address dictionary
                addresses[address_num][attribute_name] = value
    
        # Print the addresses dictionary
        contact = Contact(first_name=request.form.get('first_name'),
                          last_name=request.form.get('last_name'),
                          national_id=request.form.get('national_id'),
                          email=request.form.get('email'),
                          age=request.form.get('age'),
                          gender = True if request.form.get('gender') == '1' else False,
                          gpa=request.form.get('gpa'),
                          birthday=request.form.get('birthday'),
                          description=request.form.get('description'),
                          degree=Degree[request.form.get('degree')])
        db.session.add(contact)
        db.session.commit()
        contact = Contact.query.filter_by(national_id=request.form.get('national_id')).first()
        print(contact)
        if bool(addresses):
              for key, adrs in addresses.items():
                 address = Address(address = adrs['text'],title = adrs['title'],postal_code = adrs['postal_code'],phone = adrs['phone'],contact_id = contact.id)
                 db.session.add(address)
        db.session.commit()
        flash('Contact added successfully.')
        return redirect(url_for('contacts'))
    return render_template('add_contact.html')

@app.route("/contacts",methods=['GET'])
def contacts():
    return render_template('contacts.html',contacts = Contact.query.order_by(Contact.id).paginate(page=request.args.get('page', 1, type=int), per_page=10))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


