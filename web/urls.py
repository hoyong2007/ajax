from django.conf.urls import url
from . import views


urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^anounce/anounce.html',views.anounce, name="anounce"),
		url(r'^anounce/get_list',views.get_list, name="get_list"),
		url(r'^anounce/detail_list/(?P<num>[0-9]+)$', views.detail_list, name="detail_list"),
		url(r'^anounce/get_context/(?P<num>[0-9]+)$', views.get_context, name="get_context"),
		url(r'^contact.html$', views.contact, name="contact"),
]
