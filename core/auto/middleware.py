
from django.contrib import messages
from .models import Auto
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from django.urls import reverse
import logging

LOG = logging.getLogger(__name__)


# controllo proprietà autovetture
class OwnerCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'targa' in view_kwargs:
            targa = view_kwargs['targa']
            auto = get_object_or_404(Auto, targa=targa)
            if not auto.owner == request.user:
                LOG.warning('Accesso Proibito: Auto non di proprietà.')
                messages.error(request, 'Accesso Proibito: Auto non di proprietà.')
                return redirect(reverse('home'))
