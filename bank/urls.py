from django.contrib import admin
from django.urls import path
from bankapp.views import home, create, transfer, view_acc, history

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("create", create, name="create"),
    path("transfer", transfer, name="transfer"),
    path("view_acc", view_acc, name="view_acc"),
    path("history", history, name="history"),
]
