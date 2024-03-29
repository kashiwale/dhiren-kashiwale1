from django.db import models

# Create your models here.


class Csv(models.Model):
    #file_name = models.FileField(upload_to='csvc/', max_length=100)
    file_name = models.FileField(upload_to='media/', max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return "File id: {}".format(self.id)