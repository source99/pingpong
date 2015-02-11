from django.conf.urls import patterns, url
from pingpong import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_match/$',views.add_match,name='add_match'),
        url(r'^show_record/$',views.show_record,name='show_record'),
        url(r'^add_player/$',views.add_player,name='add_category'),
)

