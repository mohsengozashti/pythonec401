from database import getDB

db = getDB()

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    address = db.Column(db.Text(1000), nullable = False)
    title = db.Column(db.String(80),nullable = False)
    postal_code = db.Column(db.String(80),nullable = False)
    phone = db.Column(db.String(80), unique=True, nullable=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id', ondelete='CASCADE', onupdate='CASCADE'))
    def __repr__(self):
        return "<Address: {}>".format(self.address)