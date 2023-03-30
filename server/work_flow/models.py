from mongoengine import Document, fields 

# Create your models here.

class Workflow(Document):
    uuid = fields.StringField()
    wf_name = fields.StringField()
    wf_desc = fields.StringField()
    wf_user = fields.StringField()
    
    def __str__(self):
        return self.wf_name