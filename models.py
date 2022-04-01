from app import db

class Project(db.Model):
    __tablename__ = 'tb_projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    role = db.Column(db.String())
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    description = db.Column(db.String())
    created = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, name, role, start_date, end_date, description):
        self.name = name
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'role': self.role,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'created': self.created
        }
            