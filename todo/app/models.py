from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=100)
    #until = models.DateTimeField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# version 2, add goals.
# GOAL_TYPE = (
#     ('Lose Weight', 'Lose Weight'),
#     ('Gain Weight', 'Gain Weight'),
#     ('Quit Smoking', 'Quit Smoking'),
#     ('Healthy Diet', 'Healthy Diet'),
#     ('Excersice', 'Excersice'),
#     ('Learn Skill', 'Learn Skill'),
# )

# class Goal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
#     name = models.CharField(max_length=100, choices=GOAL_TYPE)
#     stepOne = models.CharField(max_length=100)
#     complete = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     slug = models.SlugField()

#     def __str__(self):
#         return str(self.name) + " <--> " + str(self.complete)
