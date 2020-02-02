from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^book/add$', views.add_book),
    url(r'^book/(?P<book_id>\d+)/show_description$', views.show_description),
    url(r'^authors$', views.authors),
    url(r'^author/add$', views.add_author),
    url(r'^author/(?P<author_id>\d+)/show_notes$', views.show_notes),
    url(r'^book/(?P<book_id>\d+)/add_additional_author$', views.add_additional_author),
    url(r'^author/(?P<author_id>\d+)/add_additional_book$', views.add_additional_book)
]
