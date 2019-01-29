from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///pupshop.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

##########_user commands_##########
def add_user (username, password):
	if username == session.query(User).filter_by(username = username).first():
		return AssertionError("the user name is already exists! choose a new one")
	user = User(username = username, password = password, addmin = False)
	session.add(user)
	session.commit()

def query_users():
	users = session.query(User).all()
	return users


def buy_puppet (name):
	pup_to_buy = session.query(Puppet).filter_by(name = name).first() 
	if pup_to_buy.amount == 0:
		return AssertionError("there are no more puppets from that type in the storge! you can choose something else :)")
	else: 
		pup_to_buy.amount = pup_to_buy.amount - 1
		session.commit()
		return True

##########_admin commands_##########
def get_user_by_username(username):
    user = session.query(User).filter_by(username = username).first()
    return user

def delete_user (username):
	session.query(User).filter_by(name = username).delete()
	session.commit()

def add_puppet (image_url, name, description, price, amount):
	if amount>0:
		puppet = Puppet(image_url = image_url, name = name, description = description, price = price, amount = amount, is_there = False)
	else:
		puppet = Puppet(image_url = image_url, name = name, description = description, price = price, amount = amount, is_there = True)
	session.add(puppet)
	session.commit()
add_puppet("sdasdasd.png", "gilad", "useless", 1, 1)
##########_showing commands_##########
def get_all_puppets():
	return session.query(Puppet).all()

##########_sign up_##########
def valid_username(username):
	names = session.query(User).filter_by(username = username).all()
	for nam in names:
		if nam.username == username:
			return False
	return True

def valid_password(password):
	if len(password)<4:
		return  False
	return True

##########_log in_##########
def valid_info(username, password):
	user = session.query(User).filter_by(username=username).first()
	if user.password == password:
		return True
	return False



