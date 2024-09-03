from djongo import models

# Create your models here.
class Notes(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=5000)
    createAt = models.DateField(auto_now=True, auto_now_add=False)
    updateAt = models.DateField()