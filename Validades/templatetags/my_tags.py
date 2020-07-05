from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def horas_real(format_string):
    return datetime.now().strftime(format_string)