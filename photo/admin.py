from django.contrib import admin
# CustomUserをインポート
from .models import Category, PhotoPost, MessagePost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #　レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    #　表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #　レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    #　表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class MessagePostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    #　レコード一覧にidとtitleを表示
    list_display = ('id', 'user_name')
    #　表示するカラムにリンクを設定
    list_display_links = ('id', 'user_name')

# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)

# Django管理サイトにMessagePost,MessagePostAdminを登録する
admin.site.register(MessagePost, MessagePostAdmin)