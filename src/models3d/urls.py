from django.conf.urls import url

from .views import ModelsView, ModelDetailView


urlpatterns = [
    url(r'^models$', ModelsView.as_view()),
    url(r'^models/(?P<name>\w+)$', ModelDetailView.as_view()),
]
