from authors_app.extensions import db,migrate



class User(db.Model):
    __table__='users'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50),nullable = False)
    last_name = db.Column(db.String(100),nullable = True)
    email = db.Column(db.String(100),nullable = False,unique = True)
    contact = db.Column(db.Integer,nullable=True)
    user_type = db.Column(db.String(20),default='author')
    user_image = db.Column(db.BOLB,nullable=True)
    biography = db.Column(db.Text,nullable=True)
    books = db.relationship('Book',backref='user')
    password_hash = db.Column(db.String(128)) #Stores the hashed password
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,first_name,last_name,email,contact,password,user_type,image):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.contact = contact
    self.password = password
    self.user_type = user_type
    self.image = image
    

def get_full_name(self):
    return f"{self.last_name}{self.first_name}"



