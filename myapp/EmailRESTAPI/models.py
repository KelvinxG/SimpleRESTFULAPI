from django.db import models

# Create your models here.
class EmailModel(models.Model):
    id=models.AutoField(primary_key=True)
    from_email = models.EmailField()
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.from_email}, To: {self.to_email}"
    