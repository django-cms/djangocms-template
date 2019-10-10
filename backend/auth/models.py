from cuser.models import AbstractCUser


class User(AbstractCUser):
    """
    The base class sets the email as username.
    """
    class Meta(AbstractCUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        abstract = False
