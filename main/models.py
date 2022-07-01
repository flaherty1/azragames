from django.db import models

# Create your models here.

class Download(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.id} | {self.ip} | {self.country} | {self.comment} | {self.created_at.strftime("%Y.%m.%d %H:%M")}'

class Code(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    link = models.TextField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.code} | {self.link} | {self.comment} | {self.created_at.strftime("%Y.%m.%d %H:%M")}'
# Setting(link="123").save()