from django.urls import path
from .views import (
    AutoListView,
    AutoCreateView,
    AutoUpdateView,
    AutoDeleteView,
    ListaDocumentoAutoView,
    CreaDocumentoAutoView,
    ModificaDocumentoAutoView,
    EliminaDocumentoAutoView,
    AutoDetailView,
    CrontabUpdateView,
    PeriodicTaskListView,
    documento_archiviato,
    documento_controllo_scadenza
)

app_name = 'auto'

urlpatterns = [

    path('', AutoListView.as_view(), name='lista_auto'),
    path('crea/', AutoCreateView.as_view(), name='crea_auto'),
    path('<str:targa>/modifica/', AutoUpdateView.as_view(), name='modifica_auto'),
    path('<str:targa>/elimina/', AutoDeleteView.as_view(), name='elimina_auto'),

    path('documenti/', ListaDocumentoAutoView.as_view(), name='lista_documento_auto'),
    path('<str:targa>/documento/crea/', CreaDocumentoAutoView.as_view(), name='crea_documento_auto'),
    path('documento/<int:pk>/modifica/', ModificaDocumentoAutoView.as_view(), name='modifica_documento_auto'),
    path('documento/<int:pk>/elimina/', EliminaDocumentoAutoView.as_view(), name='elimina_documento_auto'),
    path('documento/<int:pk>/pagato/', documento_archiviato, name='documento_archiviato'),
    path('documento/<int:pk>/scadenza/', documento_controllo_scadenza, name='controllo_scadenza'),

    path('orario-controllo/modifica', CrontabUpdateView.as_view(), name='modifica_orario_controllo'),
    path('orario-task/<int:pk>/modifica', CrontabUpdateView.as_view(), name='modifica_orario_task'),
    path('periodic-tasks', PeriodicTaskListView.as_view(), name='periodic_tasks'),

    path('<str:targa>/', AutoDetailView.as_view(), name='auto'),


]
