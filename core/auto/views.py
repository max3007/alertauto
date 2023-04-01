from django.shortcuts import get_object_or_404, redirect
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Auto, DocumentoAuto
from .forms import AutoForm, DocumentoForm
from django.contrib.messages.views import SuccessMessageMixin
import logging


LOG = logging.getLogger(__name__)


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'auto/auto_detail.html'
    context_object_name = 'auto'

    def get_object(self):
        return Auto.objects.get(targa=self.kwargs['targa'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auto = self.get_object()
        context['documenti'] = auto.documenti.all()
        return context


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/auto_list.html'
    context_object_name = 'auto_list'

    def get_queryset(self):
        # recupera l'user loggato
        user = self.request.user
        return Auto.objects.filter(owner=user)


class AutoCreateView(SuccessMessageMixin, CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'auto/auto_form.html'
    success_message = " %(auto)s con targa %(targa_auto)s Inserita Correttamente"
    success_url = reverse_lazy('auto:lista_auto')

    def form_valid(self, form):
        # Rimuovi spazi e riformatta la targa
        targa = form.cleaned_data['targa'].replace(' ', '').upper()
        form.instance.targa = targa

        form.instance.owner = self.request.user

        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            targa_auto=self.object.targa,
            auto=self.object.car_model,
        )


class AutoUpdateView(SuccessMessageMixin, UpdateView):
    model = Auto
    template_name = 'auto/auto_form.html'
    form_class = AutoForm
    success_message = " %(auto)s con targa %(targa_auto)s Aggiornata Correttamente"
    success_url = reverse_lazy('auto:lista_auto')

    def get_object(self):
        return Auto.objects.get(targa=self.kwargs['targa'])

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            targa_auto=self.object.targa,
            auto=self.object.car_model,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auto = self.object
        data_immatricolazione = None
        if auto.data_immatricolazione:
            data_immatricolazione = auto.data_immatricolazione.strftime("%Y-%m-%d")

        form = self.form_class(
            instance=auto,
            initial={"data_immatricolazione": data_immatricolazione},
        )
        context["form"] = form
        return context


class AutoDeleteView(SuccessMessageMixin, DeleteView):
    model = Auto
    template_name = 'auto/auto_delete.html'
    success_message = 'Auto Eliminata'
    success_url = reverse_lazy('auto:lista_auto')

    def get_object(self):
        return Auto.objects.get(targa=self.kwargs['targa'])


class ListaDocumentoAutoView(ListView):
    model = DocumentoAuto
    template_name = 'auto/documento_auto_list.html'
    context_object_name = 'documenti'

    def get_queryset(self):
        # recupera l'user loggato
        user = self.request.user
        return DocumentoAuto.objects.filter(auto__owner=user)


class CreaDocumentoAutoView(SuccessMessageMixin, CreateView):
    model = DocumentoAuto
    template_name = 'auto/documento_form.html'
    form_class = DocumentoForm
    success_message = 'Documento Inserito'
    success_url = reverse_lazy('auto:lista_documento_auto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auto'] = Auto.objects.get(targa=self.kwargs['targa'])
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.auto = context['auto']
        return super().form_valid(form)


class ModificaDocumentoAutoView(SuccessMessageMixin, UpdateView):
    model = DocumentoAuto
    template_name = 'auto/documento_form.html'
    form_class = DocumentoForm
    success_message = 'Documento Aggiornato'
    success_url = reverse_lazy('auto:lista_documento_auto')
    context_object_name = 'documento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documento = self.object
        data_documento = None
        data_scadenza = None
        if documento.data_scadenza:
            data_scadenza = documento.data_scadenza.strftime("%Y-%m-%d")

        if documento.data_documento:
            data_documento = documento.data_documento.strftime("%Y-%m-%d")

        form = self.form_class(
            instance=documento,
            initial={"data_documento": data_documento, "data_scadenza": data_scadenza},
        )
        context["form"] = form
        # context['auto'] = Auto.objects.get(targa=self.object.auto)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.auto = self.object.auto
        return super().form_valid(form)


class EliminaDocumentoAutoView(SuccessMessageMixin, DeleteView):
    model = DocumentoAuto
    template_name = 'auto/documento_auto_delete.html'
    success_message = 'Documento Eliminato'
    success_url = reverse_lazy('lista_documento_auto')


def documento_archiviato(request, pk):
    documento = get_object_or_404(DocumentoAuto, pk=pk)
    if documento.archiviato == True:
        documento.archiviato = False
    else:
        documento.archiviato = True
    documento.save()
    return redirect('auto:lista_documento_auto')


def documento_controllo_scadenza(request, pk):
    documento = get_object_or_404(DocumentoAuto, pk=pk)
    if documento.controllo_scadenza == True:
        documento.controllo_scadenza = False
    else:
        documento.controllo_scadenza = True
    documento.save()
    return redirect('auto:lista_documento_auto')


class CrontabUpdateView(SuccessMessageMixin, UpdateView):
    model = CrontabSchedule
    fields = "__all__"
    template_name = 'task_manager/crontab_update.html'
    success_message = 'Orario Controllo Aggiornato'
    success_url = reverse_lazy('auto:lista_auto')


class PeriodicTaskListView(ListView):
    model = PeriodicTask
    template_name = 'task_manager/periodictask_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return PeriodicTask.objects.exclude(name='celery.backend_cleanup')
