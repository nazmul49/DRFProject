from django.conf.urls import url
from .views import ContactList, ContactDeleteUpdate

urlpatterns = [
    url(r'^api/v1/contact/$', ContactList.as_view()),
    url(r'^api/v1/contact/(?P<contact_id>[0-9])/$', ContactDeleteUpdate.as_view())
]
