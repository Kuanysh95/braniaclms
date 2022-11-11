from django import template
from django.utils.safestring import mark_safe

register = template.library()


@register.filter
def email_to_link(email_string):
    return mark_safe(f"<a href='mailto:{email_string}'>{email_string}</a>")