from flask import Flask
from flask_sqlalchemy import SQLAlchemy

Task = Flask(__name__)
Task.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///tasks.db'
db = SQLAlchemy(Task)
db.init_app(Task)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

db.create_all()
