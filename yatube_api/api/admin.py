from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'group', 'pub_date')
    list_filter = ('pub_date', 'group')
    search_fields = ('text', 'author__username')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'post', 'created')
    list_filter = ('created',)
    search_fields = ('text', 'author__username', 'post__text')
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user',)
