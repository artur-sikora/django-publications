__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.conf.urls import url
from django.contrib import admin
from publications.admin_views import import_bibtex
from publications.models import CustomFile, CustomLink


class CustomLinkInline(admin.StackedInline):
	model = CustomLink
	extra = 1
	max_num = 5


class CustomFileInline(admin.StackedInline):
	model = CustomFile
	extra = 1
	max_num = 5


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('type', 'first_author', 'title', 'type', 'year', 'journal_or_book_title')
    list_display_links = ('title',)
    change_list_template = 'admin/publications/publication_change_list.html'
    search_fields = ('title', 'journal', 'authors', 'keywords', 'year')
    fieldsets = (
            (None, {'fields':
                    ('type', 'title', 'authors', 'year', 'month')}),
            (None, {'fields':
                    ('journal', 'book_title', 'publisher', 'institution', 'volume', 'number', 'pages')}),
            (None, {'fields':
                    ('citekey', 'keywords', 'url', 'code', 'pdf', 'doi', 'isbn', 'note', 'external')}),
            (None, {'fields':
                    ('abstract',)}),
            (None, {'fields':
                    ('image', 'thumbnail')}),
            (None, {'fields':
                    ('lists',)}),
    )
    inlines = [CustomLinkInline, CustomFileInline]

    def get_urls(self):
            return [url(r'^import_bibtex/$', import_bibtex,
                    name='publications_publication_import_bibtex'),] + super(PublicationAdmin, self).get_urls()
