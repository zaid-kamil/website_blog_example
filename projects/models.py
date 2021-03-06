from django.db import models

# Create your models here.
class Project(models.Model):
    """Model definition for Project."""
    title = models.CharField(max_length=100,default='project')
    description = models.TextField(default='No Description given')
    technology = models.CharField(max_length=50, default='Django')
    img = models.ImageField(upload_to='projects/', default='projects/noimg.jpg')

    class Meta:
        """Meta definition for Project."""
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Unicode representation of Project."""
        return self.title
