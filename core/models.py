from django.db import models


class CV(models.Model):
    file = models.FileField(upload_to="cv/")
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ContactUs(models.Model):
    sender_name = models.CharField(max_length=70, null=True, blank=True)
    sender_email = models.CharField(max_length=70, null=True, blank=True)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timeStamp"]
        verbose_name = "Contact Us Massage"
        verbose_name_plural = "Contact Us Massages"

    def __str__(self):
        return str(self.sender_name)
