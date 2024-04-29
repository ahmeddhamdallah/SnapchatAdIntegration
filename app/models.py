from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    segment_id = db.Column(db.String(100), nullable=False)  # Snapchat segment ID

    def __repr__(self):
        return f'<User {self.username}>'
