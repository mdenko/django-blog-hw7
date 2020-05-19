from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category

class PostInline(admin.TabularInline):
    model = Post

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine,
    ]
    exclude = ('Post',)

class PostAdmin(admin.ModelAdmin):
    inlines = [PostInLine,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
