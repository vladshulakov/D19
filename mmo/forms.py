from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_text',
            'category',
        ]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'post',
            'reply_text',
        ]