from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<question_id>[0-9]+$)',views.detail, name='detail'),
    url(r'^add$',views.add, name='add'),
    url(r'^update/(?P<question_id>[0-9]+$)',views.update, name='update'),
]

handler404 = 'polls.views.handler404'
handler500 = 'polls.views.handler500'