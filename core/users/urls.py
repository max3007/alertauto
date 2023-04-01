from django.urls import path
from django.contrib import admin


from core.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]


admin.site.site_header = "Amministrazione Alert Auto"
admin.site.site_title = "Amministrazione Alert Auto"
admin.site.index_title = "Amministrazione Alert Auto"
