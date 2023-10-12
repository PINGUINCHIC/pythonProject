from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    words = value.split()
    STOP_LIST = [
        'мат',
        'мат',
        'Dropbox',
    ]
    for w in words:
        if w in STOP_LIST:
            value = value.replace(w,'*' * len(w))
    return value