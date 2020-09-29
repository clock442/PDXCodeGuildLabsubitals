from django.db import models

class Priority(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField()
    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    description = models.CharField(max_length=200)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todoitems')
    def __str__(self):
        return self.description + ' ' + self.created_date.strftime('%Y-%m-%d')






