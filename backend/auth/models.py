from cuser.models import AbstractCUser
from django.db.models import CharField


class User(AbstractCUser):
    """
    The base of this class cuser.AbstractCUser sets the email as username.
    """

    #: This field is required by cms.PageUserAdmin, because that class
    #: violets its own bloody documentation. Otherwise this field is useless.
    username = CharField(
        max_length=128,
        blank=True,
        help_text='Serves only cosmetic purpose, can be ignored',
    )

    class Meta(AbstractCUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        abstract = False
