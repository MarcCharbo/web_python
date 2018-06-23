from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    # username = CharField(primary_key = True, max_length = 30)
    # password = CharField(max_length = 30)
    # user_first_name = CharField(max_length = 30)
    # user_last_name = CharField(max_length = 30)

    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)


class Task(BaseModel):
    # task_id = CharField(unique=True)
    # task_start_time = DateTimeField(formats = 'YYYY-mm-dd HH:MM:SS')
    # task_end_time = DateTimeField(formats = 'YYYY-mm-dd HH:MM:SS')
    # task_description = CharField(max_length = 140)
    # username = ForeignKeyField(User, backref='tasks')
    
    name = CharField(max_length=255)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)