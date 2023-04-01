
from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from django.urls import reverse
import logging

LOG = logging.getLogger(__name__)

EXEMPT_URLS = [reverse('account_signup')]
if hasattr(settings, 'AUTH_EXEMPT_URLS'):
    EXEMPT_URLS += settings.AUTH_EXEMPT_URLS


class AuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path.lstrip('/')

        for exempt_url in EXEMPT_URLS:
            if request.path.startswith(exempt_url):
                response = self.get_response(request)
                return response

        if path == settings.ADMIN_URL.lstrip('/') and not request.user.is_authenticated:
            return redirect(reverse('admin:login'))

        if not request.user.is_authenticated:
            if not request.path.startswith(reverse('account_login')) and not request.path.startswith(reverse('admin:login')):
                return redirect(reverse('account_login') + '?next=' + request.path)

        response = self.get_response(request)
        return response
