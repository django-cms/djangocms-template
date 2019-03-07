from django.apps.registry import Apps
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def add_default_admin_for_testing_on_non_prod_env(apps: Apps, _):
    """
    Note: such methods as `create`, `create_superuser` and `set_password` aren't
    going to work in migrations.
    """
    is_prod_env = settings.ENVIRONMENT == 'prod'
    if is_prod_env:
        return

    User = apps.get_model('custom_user', 'User')
    email_and_pass = 'test@what.digital'
    if User.objects.filter(email=email_and_pass).exists():
        return
    # `create_superuser` and `set_password` aren't going to work in migrations
    user = User(
        email=email_and_pass,
        is_staff=True,
        is_superuser=True,
    )
    user.password = make_password(email_and_pass)
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(add_default_admin_for_testing_on_non_prod_env),
    ]
