from django.utils import timezone
from core.auto.models import DocumentoAuto, Auto


def documenti_context_processor(request):
    user = request.user
    if user.is_authenticated:
        documenti = DocumentoAuto.objects.filter(auto__owner=user)
        return {'documenti': documenti}
    return request


def documenti_scaduti_context_processor(request):
    user = request.user
    if user.is_authenticated:
        documenti_scaduti = DocumentoAuto.objects.filter(
            auto__owner=user).filter(scaduto=True).filter(archiviato=False)
        return {'documenti_scaduti': documenti_scaduti}
    return {}


def auto_context_processor(request):
    user = request.user
    if user.is_authenticated:
        auto = Auto.objects.filter(owner=user)
        return {'auto': auto}
    return {}
