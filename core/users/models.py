from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.utils.fields import PrivateFileField


class User(AbstractUser):
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(
        _("Nome"),
        blank=True,
        max_length=255
    )
    avatar = models.FileField(
        _("Foto"),
        upload_to='avatar/',
        max_length=100,
        null=True,
        blank=True)

    first_name = None  # type: ignore
    last_name = None  # type: ignore

    file = models.FileField(_("File"), upload_to="documenti_user", max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        self.name = str.title(self.name)
        super(User, self).save(*args, **kwargs)
