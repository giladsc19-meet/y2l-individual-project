from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Puppet(Base):
    __tablename__ = 'puppets'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    amount = Column(Integer)
    is_there = Column(Boolean)
    def __repr__(self):
        return "\n image_url: " + self.image_url + "\nname: " + self.name + "\ndescription: " + self.description + "\nprice: " + str(self.price) + "\namount: " + str(self.amount) + "\nis_there: " + str(self.is_there)
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    addmin = Column(Boolean)
    def __repr__(self):
        return "\nusername: " + self.username + "\npassword: " + self.password + "\nis admin: " + str(self.addmin) + "\n"

