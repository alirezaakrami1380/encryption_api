from peewee import Model, TextField, DateTimeField
from datetime import datetime
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class Message(BaseModel):
    encrypted = TextField()
    created_at = DateTimeField(default=datetime.now)

def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([Message])
    print("دیتابیس آماده است")
    db.close()

if __name__ == '__main__' :
    init_db()