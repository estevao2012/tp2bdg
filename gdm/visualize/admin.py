from django.contrib import admin
from visualize.models import Poll,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  list_display = ('question', 'pub_date', 'was_published_today')
  inlines = [ChoiceInline]
  search_fields = ['question']
  list_filter = ['pub_date']
  date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)