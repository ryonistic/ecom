from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class StoreConfig(AppConfig):
    name = "ecom.store"
    verbose_name = _("Store")
    default_auto_field = 'django.db.models.BigAutoField'
