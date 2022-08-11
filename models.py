import db


class User(db.BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    __table_name__ = 'user'

    def repr(self):
        return '<User {id}>'


class Candidate(db.BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    when = db.Column(db.DateTime)
    event = db.relationship('Event')
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))


class Attendance(db.BaseModel):
    user = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    candidate = db.relationship('Candidate')
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"))
    event = db.relationship('Event')
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))


class Event(db.BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    host = db.relationship('User')
