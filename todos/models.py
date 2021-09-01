from django.db import models

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.TextField(max_length=30,null=False,unique=True)
    password=models.TextField(max_length=30,null=False)
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id=models.IntegerField(null=False)
    title=models.TextField(max_length=100,null=False)
    complete=models.BooleanField(null=False,default=False)
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
    """