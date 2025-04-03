from django import forms

from .models import Volonteer

class PostForm(forms.ModelForm):

    class Meta:
        model = Volonteer
        fields = ('title', 'text',)