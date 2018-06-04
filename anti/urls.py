from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.index,name='index'),
    url('^about/',views.about,name='about'),
    url('^comment/',views.comment,name='comment'),
    url(r'^report/',views.new_comment,name='new_comment'),
    url(r'^categorys/',views.view_category,name='category'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
