from django.contrib import admin

from .models import Article

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "user"]

	search_fields = ["title", "content"]
	class Meta:
		model = Article


admin.site.register(Article, PostModelAdmin)
