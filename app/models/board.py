from app import db
from flask import current_app

class Board(db.Model):
    __tablename__="board"
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship('Card', backref='board', lazy=True)

    def to_json(self):
        return{
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }