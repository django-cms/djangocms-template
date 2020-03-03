from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django_settings_export import settings_export


def send_email(
    subject: str,
    template_plaintext_path: str,
    template_html_path: str,
    template_context: dict = None,
    email_destination: str = None,
):
    template_plaintext = get_template(template_plaintext_path)
    template_context = _get_full_context(context_base=template_context)
    email = EmailMultiAlternatives(
        subject=subject,
        body=template_plaintext.render(template_context),
        from_email=settings.BUSINESS_EMAIL_VANE,
        to=[email_destination],
    )
    template_html = get_template(template_html_path)
    email.attach_alternative(template_html.render(template_context), 'text/html')
    email.send()


def _get_full_context(context_base: dict = None) -> dict:
    settings_exported = settings_export(request=None)
    if context_base is None:
        return settings_exported
    else:
        return {**context_base, **settings_exported}
