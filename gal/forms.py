

from django import forms
from django.core.exceptions import ValidationError


class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            file_extension = image.name.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png']:
                raise ValidationError(
                    "Only JPG, JPEG, and PNG files are allowed.")

        return image
