from django import forms
from django.contrib.auth.models import User
from .models import Comments

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = ''
        self.fields['text'].widget.attrs['placeholder'] = 'Add Comments'

    class Meta:
         model = Comments
         fields = ['text']



