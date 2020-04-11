from django import forms
from django.core.validators import FileExtensionValidator

from .models import UploadFile


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["jpg", ])]
    )


class UploadFileModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = "__all__"
