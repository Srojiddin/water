from django import forms
from django.forms import inlineformset_factory
from apps.news.models import News, Images

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image',)
        widgets = {'image': forms.ClearableFileInput(attrs={
                                            'class': 'form-control'
        })}


NewsImagesFormSet = inlineformset_factory(News, Images, form=ImagesForm, extra=1, max_num=5)


class NewsCreateForm(forms.ModelForm):
    images = NewsImagesFormSet()

    class Meta:
        model = News
        fields = ('description', 'title')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '4'})