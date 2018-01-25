from django.db import models

# Create your models here.
class Comment(models.Model):
    user_name=models.CharField(max_length=20)
    titleId=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering=['-date_time']