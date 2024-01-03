from django import forms
from utils.admin import FileContentPreviewWidget

from personal_training.files.models.models import File  # Replace with the actual model name


class YourModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"

    file = forms.FileField(widget=FileContentPreviewWidget)
