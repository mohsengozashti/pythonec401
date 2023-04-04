from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Text, Integer, String, DateTime, Numeric, SmallInteger,ForeignKey
from sqlalchemy import SQLAlchemy
Base = declarative_base()
class address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    address = Column(Text(1000), nullable = False)
    title = Column(String(80),nullable = False)
    postal_code = Column(String(80),nullable = False)
    phone = Column(String(80), unique=True, nullable=True)
    contact_id = Column("user_id", Integer, ForeignKey("contacts.id"), nullable=False),
    def __repr__(self):
        return "<Address: {}>".format(self.address)