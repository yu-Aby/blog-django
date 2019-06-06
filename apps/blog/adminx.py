

from xadmin import views
import xadmin
from .models import  User, Tag, Category, Comment, Article, ArticleManager, Links


class ThemeAdmin():
    enable_themes = True
    use_bootswatch = True

class GlobalSettings():
    site_title = "梵宇墨"
    site_footer = "yu"

class UserAdmin():
    list_display = ['username','email','avatar']



class TagAdmin():
    list_display = ['name']



class CategoryAdmin():
    list_display = ['name','index']



class ArticleAdmin():
    list_display = ['title', 'desc','content','click_count',
                    'comment_count','date_publish','user','category','tag']
    search_fields = ['title', 'desc','content']
    list_filter = ['title', 'desc','content','date_publish']
    style_fields = {'content':'ueditor'}






class CommentAdmin():
    list_display = ['content','username','email','date_publish','user','article','pid']



class LinksAdmin():
    list_display = ['title','description','callback_url','date_publish','index']

xadmin.site.unregister(User)
xadmin.site.register(User,UserAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(Links,LinksAdmin)
xadmin.site.register(views.BaseAdminView, ThemeAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)