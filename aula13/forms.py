from django import forms
from .models import UploadFile
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["jpg", ])]
    )


class UploadFileModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = "__all__"