"""Seed database with sample data from CSV Files."""

from models import User, Workspace, db
from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt()


# Create all tables
db.create_all()

# If table are not empty, empty them
User.query.delete()
Workspace.query.delete()

# Add users
hashed_pwd = bcrypt.generate_password_hash("testtest").decode('UTF-8')
u1 = User(first_name="Jon", last_name="Snow", email="jsnow@winterfell.com", username="jsnow", password=hashed_pwd)
u2 = User(first_name="Jamie", last_name="Lannister", e  mail="jlannister@rock.com", username="jlannister", password=hashed_pwd)


# Add workspaces
w1 = Workspace(formatted_name="my.first.workspace", readable_name="My First Workspace")
w2 = Workspace(formatted_name="spotify", readable_name="Spotify")

# Add new objects to session, so they'll persist
db.session.add(u1)
db.session.add(u2)
db.session.add(w1)
db.session.add(w2)

# Commit--otherwise, this never gets saved!
db.session.commit()