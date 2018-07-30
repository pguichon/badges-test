# coding=utf-8
from datetime import timedelta
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from badges.models import Pioneer


def pioneer_user(sender, user, request, **kwargs):
    """
    Signal to create a Pionner entry when a user logged in
    We can do that with a crontab or a celery task
    """
    if (user.date_joined + timedelta(days=365)) <= timezone.now():
        Pioneer.objects.get_or_create(user=user)

user_logged_in.connect(pioneer_user)
