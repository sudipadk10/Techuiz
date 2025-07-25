import uuid
from django.db import models


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Category(BaseModel):
    category_name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.category_name
    
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.TextField()
    marks = models.IntegerField(default=1)
    def __str__(self):
        return self.question
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete= models.CASCADE)
    answer = models.CharField()
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer