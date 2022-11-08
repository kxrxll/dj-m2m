from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter is not 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
