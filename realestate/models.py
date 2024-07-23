from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    roi = models.DecimalField(max_digits=5, decimal_places=2, help_text="Return on Investment (ROI) percentage")

    def __str__(self):
        return self.name
