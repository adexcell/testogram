from django.contrib import admin
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from general.filters import AuthorFilter, PostFilter
from general.models import (
    Post,
    User,
    Comment,
    Reaction,
)


admin.site.unregister(Group)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )
    # fields = (
    #     "first_name",
    #     "last_name",
    #     "username",
    #     "password",
    #     "email",
    #     "is_staff",
    #     "is_superuser",
    #     "is_active",
    #     "friends",
    #     "date_joined",
    #     "last_login",
    # )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    fieldsets = (
        (
            "Личные данные", {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            }
        ),
        (
            "Учетные данные", {
                "fields": (
                    "username",
                    "password",
                )
            }
        ),
        (
            "Статусы", {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                )
            }
        ),
        (
            None, {
                "fields": (
                    "friends",
                )
            }
        ),
        (
            "Даты", {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            }
        )
    )
    
    search_fields = (
        "id",
        "username",
        "email",
    )
    
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        ("date_joined", DateRangeFilter),
    )


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "get_body",
        "get_comment",
        "created_at",
    )
    
    fields = (
        "title",
        "body",
        "author",
        "created_at",
        "get_comment",
    )
    
    readonly_fields = (
        "created_at",
        "get_comment",
    )
    
    list_display_links = (
        "id", 
        "get_body",
    )
    
    search_fields = (
        "id",
        "title",
    )
    
    list_filter = (
        AuthorFilter,
        ("created_at", DateRangeFilter),
    )
    
    def get_body(self, obj):
        max_length = 64
        if len(obj.body) > max_length:
            return obj.body[:61] + "..."
        return obj.body
    
    get_body.short_description = "body"
    
    def get_comment(self, obj):
        return obj.comments.count()
    
    get_comment.short_description = "comments count"


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "get_post_title",
        "post",
        "body",
        "created_at",
    )
    
    fields = (
        "post",
        "body",
        "author",
        "get_post_title",
    )
    
    readonly_fields = (
        "get_post_title",
    )
    
    list_display_links = (
        "id",
        "body",
        "get_post_title",
    )
    
    list_filter = (
        AuthorFilter,
        PostFilter,
    )
    
    def get_post_title(self, obj):
        return obj.post.title
    
    get_post_title.short_description = "Post title"


@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
        "author",
        "post",
    )
    
    list_display_links = (
        "id",
        "value",
    )
    
    list_filter = (
        AuthorFilter,
        PostFilter,
        "value",
    )