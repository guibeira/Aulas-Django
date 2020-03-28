from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class UploadFile(models.Model):
    name = models.CharField(max_length=30)
    file = models.ImageField(upload_to="uploads", validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "png"])
    ])