from django.conf.urls import url

from .views import ContactList, ContactDeleteUpdate

urlpatterns = [
    url(r'^contact/$', ContactList.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)/$', ContactDeleteUpdate.as_view())
]