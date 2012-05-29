from django.forms import ModelForm
from emily.main.models import UploadedImage

class ImageUploadForm(ModelForm):
    class Meta:
        model = UploadedImage