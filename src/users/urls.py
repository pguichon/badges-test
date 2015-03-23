from django.conf.urls import url

from .views import UserListView, UserDetailView


urlpatterns = [
    url(r'^users$', UserListView.as_view()),
    url(r'^users/(?P<username>\w+)$', UserDetailView.as_view()),
]
