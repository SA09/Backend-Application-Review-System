from django.db import models


class Candidate(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    address=models.TextField()
    status = models.CharField(max_length=20 ,default = "Applied")

    def __str__(self):
        return self.full_name
