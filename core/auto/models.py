import random
import string
import os
from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from PIL import Image
import io
import uuid

User = get_user_model()


def auto_file_path(instance, filename):
    """Genera il percorso del file caricato"""
    random_string = uuid.uuid4().hex[:4]
    ext = filename.split('.')[-1]
    new_filename = f"{instance.targa}_{random_string}.{ext}"
    return os.path.join('veicoli', new_filename)


class Auto(models.Model):
    class Stato(models.TextChoices):
        IN_CIRCOLAZIONE = 'IN', _('In Circolazione')
        ROTTAMATA = 'RT', _('Rottamata')
        VENDUTA = 'VE', _('Venduta')
        RUBATA = 'RU', _('Rubata')
        FERMA = 'FE', _('Ferma')

    stato = models.CharField(
        max_length=2,
        choices=Stato.choices,
        default=Stato.IN_CIRCOLAZIONE,
        help_text=_('controllo dei documenti solo se in circolazione')
    )

    class Tipo(models.TextChoices):
        AUTOVETTURA = 'AV', _('Autovettura')
        MOTOVETTURA = 'MV', _('Motovettura')
        CICLOMOTORE = 'CM', _('Ciclomotore')
        AUTOCARRO = 'AC', _('Autocarro')
        RIMORCHIO = 'RI', _('Rimorchio')

    tipo = models.CharField(
        max_length=2,
        choices=Tipo.choices,
        default=Tipo.AUTOVETTURA,
    )

    class Carburante(models.TextChoices):
        SCELTA_CARBURANTE = "", _('Scelta Carbrante')
        BENZINA = 'BE', _('Benzina')
        DIESEL = 'DI', _('Diesel')
        IBRIDA = 'IB', _('Ibrida')
        ELETTRICA = 'EL', _('Elettrica')

    carburante = models.CharField(
        max_length=2,
        choices=Carburante.choices,
        blank=True, null=True
    )

    marca = models.CharField(_("Marca"), max_length=100, blank=True, null=True)
    car_model = models.CharField(_("Modello Auto"), max_length=100, blank=True, null=True)
    targa = models.CharField(max_length=100, unique=True)
    data_immatricolazione = models.DateTimeField(blank=True, null=True)
    cilindrata = models.CharField(_("Cilindrata"), max_length=50, blank=True, null=True)
    potenza = models.CharField(_("Potenza in kW o CV"), max_length=50, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, verbose_name=_("proprietario"),
                              related_name="proprietario", on_delete=models.CASCADE)
    image_main = models.ImageField(_("Immagine Auto"), upload_to=auto_file_path, blank=True, null=True)
    image_thumb = models.ImageField(upload_to='alertauto/', blank=True, null=True)
    file = models.FileField(_("File Auto"), upload_to=auto_file_path, max_length=100, blank=True, null=True)
    note = models.TextField(_("Note Auto"), blank=True, null=True)

    class Meta:
        ordering = ('marca',)
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'

    def __str__(self):
        return f"{self.car_model} - {self.targa}"

    @property
    def reg_date_gma(self):
        return self.reg_date.strftime("%d %b %y")

    @property
    def data_immatricolazione_gma(self):
        if self.data_immatricolazione:
            return self.data_immatricolazione.strftime("%d %b %y")
        return self.data_immatricolazione

    @property
    def documenti_regolari(self):
        documenti = self.documenti.all()
        for documento in documenti:
            if documento.scaduto:
                return False
        return True

    @property
    def documenti_scaduti(self):
        documenti_scaduti = self.documenti.filter(
            Q(scaduto=True) &
            Q(archiviato=False) &
            Q(controllo_scadenza=True) &
            Q(senza_scadenza=False)
        )
        return documenti_scaduti

    def save(self, *args, **kwargs):
        self.car_model = self.car_model.capitalize()
        self.targa = self.targa.upper().replace(" ", "")
        if self.image_main:
            image = Image.open(self.image_main)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image.thumbnail((100, 100))
            image_io = io.BytesIO()

            if self.image_main.name.endswith('.png'):  # controlla il formato dell'immagine
                image.save(image_io, format='PNG')  # salva l'immagine in formato PNG
                self.image_thumb = InMemoryUploadedFile(
                    image_io, None, self.image_main.name+"_thumb.png", 'image/png',
                    image_io.tell(), None
                )
            else:
                image.save(image_io, format='JPEG')
                self.image_thumb = InMemoryUploadedFile(
                    image_io, None, self.image_main.name+"_thumb.jpeg", 'image/jpeg',
                    image_io.tell(), None
                )
        else:
            self.image_thumb = None
        super().save(*args, **kwargs)


def documento_auto_file_path(instance, filename):
    """Genera il percorso del file caricato"""
    random_string = uuid.uuid4().hex[:4]
    ext = filename.split('.')[-1]
    new_filename = f"{instance.nome}_{instance.numero}_{random_string}.{ext}"
    return os.path.join('documenti_auto', new_filename)


class DocumentoAuto(models.Model):
    nome = models.CharField(_("Nome Documento"), max_length=100)
    numero = models.CharField(_("Numero Documento"), max_length=100, blank=True, null=True,
                              help_text=_('se assente verrà auto assegnato'))
    note = models.TextField(_("Note Documento"), blank=True, null=True)
    data_documento = models.DateField(blank=True, null=True)
    data_scadenza = models.DateField(blank=True, null=True, help_text=_('senza scadenza non verrà monitorato'))
    auto = models.ForeignKey(Auto, related_name="documenti", on_delete=models.CASCADE)
    file = models.FileField(_("Allegato al Documento"), upload_to=documento_auto_file_path,
                            max_length=100, blank=True, null=True)
    senza_scadenza = models.BooleanField(_("Senza Scadenza"), default=False)
    controllo_scadenza = models.BooleanField(_("Controlo Scadenza"), default=True,
                                             help_text=_('check per non monitorare questo documento'))
    scaduto = models.BooleanField(_("Documento Scaduto"), default=False)
    archiviato = models.BooleanField(_("Documento Archiviato"), default=False)

    class Meta:
        ordering = ('data_scadenza',)
        verbose_name = 'Documento'
        verbose_name_plural = 'Documenti'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.data_scadenza:
            self.senza_scadenza = True
        else:
            self.senza_scadenza = False

        if self.data_scadenza and not self.senza_scadenza:
            self.scaduto = timezone.now().date() >= self.data_scadenza

        if not self.numero:
            # Genera un numero casuale di 5 caratteri
            numero_casuale = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            # Assegna il numero del documento
            self.numero = numero_casuale

        super().save(*args, **kwargs)

    @ property
    def data_documento_gma(self):
        if self.data_documento:
            return self.data_documento.strftime("%d %b %y")

    @ property
    def data_scadenza_gma(self):
        if self.data_scadenza:
            return self.data_scadenza.strftime("%d %b %y")


def allegato_transazione_path(instance, filename):
    """Genera il percorso del file caricato"""
    ext = filename.split('.')[-1]
    new_filename = f"{instance.documento.nome}_{instance.data_registrazione}.{ext}"
    return os.path.join('transazioni', new_filename)


class TransazioneDocumento(models.Model):
    documento = models.ForeignKey("auto.DocumentoAuto", verbose_name=_(
        "Documento"), related_name="transazioni", on_delete=models.CASCADE)
    data_transazione = models.DateField(_("Data Transazione"))
    importo = models.DecimalField(_("Importo"), max_digits=10, decimal_places=2)
    descrizione = models.TextField(_("Descrizione"), blank=True, null=True)
    data_registrazione = models.DateTimeField(_("Data Registrazione"), auto_now_add=True)
    allegato = models.FileField(_("Allegato al Documento"), upload_to=allegato_transazione_path,
                                max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.documento} {self.data_transazione}"

    class Meta:
        managed = True
        verbose_name = 'Transazione Documento'
        verbose_name_plural = 'Transazioni Documento'
