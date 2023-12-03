
from django import forms
from .models import Review


class ReviewWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['content'].label = '내용'
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = Review
        fields = ['title', 'content']
