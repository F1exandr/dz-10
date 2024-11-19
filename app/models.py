import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    password = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)


with app.app_context():
        db.create_all()