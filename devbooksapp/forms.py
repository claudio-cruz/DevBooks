"""File for all the app main forms."""

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Disply the book comment form."""

    body = forms.CharField(label='Comment:',
        widget=forms.Textarea(attrs={'rows': 4, 'minlength': 10}))

    class Meta:
        """Provide aditional information about the Comment."""
        
        model = Comment
        fields = ('body',)
