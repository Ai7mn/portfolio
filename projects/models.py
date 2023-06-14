from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class Project(models.Model):
    image = models.ImageField(upload_to='images/',
                              height_field='height',
                              width_field='width')
    height = models.PositiveIntegerField(editable=False)
    width = models.PositiveIntegerField(editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)
    check_btn = models.CharField(max_length=100, default="Check Live", blank=True, null=True)
    local = models.BooleanField(default=True)
    content = models.TextField(blank=True, null=True)
    display_order = models.IntegerField(max_length=10, default=1)
    slug = models.SlugField(max_length=200, null=True, blank=True, allow_unicode=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        unique_together = ('name', 'slug')
        ordering = ['display_order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("single_project", kwargs={"slug": str(self.slug)})

    def get_content(self):
        return mark_safe(self.content)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/images', null=True, blank=True, verbose_name='Project Image')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.name} - {self.title}"


class CV(models.Model):
    file = models.FileField(upload_to='cv/')
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
