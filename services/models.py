from django.db import models

# Create your mofrom django.db import models

class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
