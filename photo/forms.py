from django.forms import ModelForm
from .models import PhotoPost, MessagePost

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = PhotoPost
        fields = ['category','title','comment','image1','image2',]

class MessagePostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
            model: モデルのクラス
            exclude: フォーム画面に表示させないよう除外
        '''
        model = MessagePost
        exclude = ('target', 'created_at')