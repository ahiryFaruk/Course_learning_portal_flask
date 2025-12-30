from app import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50))
    level = db.Column(db.String(50))

    def __repr__(self):
        return f"<Course {self.title}>"
