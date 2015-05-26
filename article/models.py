from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=2000)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    linkes = models.IntegerField()
    
    def __unicode__(self):
        return self.title
