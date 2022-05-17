from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ecom.store.models import Cart


class User(AbstractUser):
    """
    Default custom user model for ecom.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user = User.objects.get(username=self.username)
        try:
            cart = Cart.objects.get(owner=user)
            cart.save()
        except ObjectDoesNotExist:
            cart = Cart.objects.create(owner=user)
            cart.save()

