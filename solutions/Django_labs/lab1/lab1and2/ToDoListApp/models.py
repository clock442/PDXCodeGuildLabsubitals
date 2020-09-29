from django.db import models

class ToDoItem(models.Model):
    todo_text = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return self.todo_text + ' ' + self.created_date.strftime('%Y-%m-%d')