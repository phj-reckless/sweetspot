
from django import forms
from .models import Bakery


class BakeryWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BakeryWriteForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '가게명'
        self.fields['name'].widget.attrs.update({
            'placeholder': '가게명을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['info'].label = '소개'
        self.fields['info'].widget.attrs.update({
            'placeholder': '소개를 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['hp'].label = '전화번호'
        self.fields['hp'].widget.attrs.update({
            'placeholder': '전화번호를 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['operated_date'].label = '운영시간'
        self.fields['operated_date'].widget.attrs.update({
            'placeholder': '운영시간을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['address'].label = '주소'
        self.fields['address'].widget.attrs.update({
            'placeholder': '주소를 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = Bakery
        fields = ['name', 'info', 'hp', 'operated_date', 'address']