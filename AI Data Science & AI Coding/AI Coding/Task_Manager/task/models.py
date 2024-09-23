# from djongo import models
from datetime import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField, ObjectIdField
from bson import ObjectId

# Create your models here.

class Task(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)  
    title = StringField(max_length=200, required=True)       
    description = StringField(max_length=200, required=True) 
    completed = BooleanField(default=False)                  
    created_at = DateTimeField(default=None)                 
    completed_at = DateTimeField(default=None, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()  # Set created_at when the document is first saved
        if self.completed and not self.completed_at:
            self.completed_at = datetime.utcnow()  # Set completed_at when task is marked as completed
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.description}"
    
    def __dict__(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }
        
    class Meta:
        db_table = 'task'