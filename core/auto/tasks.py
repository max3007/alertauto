import os
from datetime import timedelta
from mimetypes import guess_type

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.conf import settings

from config import celery_app
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from .models import DocumentoAuto

logger = get_task_logger(__name__)


# cambia lo stato di un documento in scaduto
@celery_app.task(name='auto.set_scaduto')
def set_scaduto():
    logger.info('Inizio esecuzione task "set_scaduto"')
    print("App Set Scadenza Orario")
    documenti = DocumentoAuto.objects.filter(scaduto=False, senza_scadenza=False,
                                             data_scadenza__lt=timezone.now().date())
    num_documenti_scaduti = documenti.count()
    for documento in documenti:
        documento.scaduto = True
        documento.save()

    logger.info('Fine esecuzione task "set_scaduto". %d documenti scaduti', num_documenti_scaduti)


# invia una mail in caso di documento scaduto
@celery_app.task(name='auto.controllo')
def controllo_scadenza():
    print("App Controllo Documento Scaduto")
    logger.info('Inizio esecuzione task "controllo_scadenza"')
    documenti = DocumentoAuto.objects.filter(controllo_scadenza=True, scaduto=True)
    num_documenti_scaduti = documenti.count()
    for documento in documenti:
        send_email(documento)
    logger.info('Fine esecuzione task "controllo_scadenza". %d mail inviate', num_documenti_scaduti)


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0),
        set_scaduto.s(),
        name='Set Scaduto')
    sender.add_periodic_task(
        crontab(hour=0, minute=5),
        controllo_scadenza.s(),
        name='Controllo Scadenza')


def send_email(documento):
    # Recupera l'auto e il proprietario del documento passato come parametro
    auto = documento.auto
    owner = auto.owner
    # Definisce il mittente e l'oggetto dell'email
    from_email = {settings.DEFAULT_FROM_EMAIL}
    subject = f'Documento {documento.nome} Auto {auto.car_model} Targa {auto.targa} Scaduto'
    # Definisce i destinatari dell'email, composto dall'email del proprietario e dalle email presenti nella tabella EmailAddress relative al proprietario
    to_emails = [owner.email] + [email.email for email in owner.emailaddress_set.all()]
    # Definisce il contesto dell'email
    context = {'documento': documento}
    # Genera il contenuto html e testuale dell'email a partire dai template html e txt
    html_content = render_to_string('email/documento_scaduto_html.html', context)
    txt_content = render_to_string('email/documento_scaduto_txt.html', context)
    # Rimuove le eventuali tags html dal testo dell'email
    text_content = strip_tags(txt_content)
    # Crea un oggetto EmailMultiAlternatives con il contenuto testuale e html dell'email, il mittente e i destinatari
    email = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    email.attach_alternative(html_content, 'text/html')
    # Se il documento ha un allegato, lo allega all'email
    if documento.file:
        content_type = guess_type(documento.file.name)
        email.attach(documento.file.name, documento.file.read(), content_type[0])
    # Invia l'email
    email.send()
