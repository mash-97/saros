from django import forms
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget
from posts.models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'text']
        widgets = {
            'text': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}})
        }
