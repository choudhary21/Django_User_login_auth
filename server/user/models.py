from mongoengine import Document, fields 

# Create your models here.

class User(Document):
    uuid = fields.StringField()
    fname = fields.StringField()
    lname = fields.StringField()
    email = fields.EmailField()
    is_admin = fields.BooleanField()
    
    def __str__(self):
        return self.fname