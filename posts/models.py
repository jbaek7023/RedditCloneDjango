from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    pub_date = models.DateField()
    author = models.ForeignKey(User)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d, %Y')
