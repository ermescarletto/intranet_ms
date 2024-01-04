from django import template
from backend.utils import encode_id  # Importe a função 'encode_id' de onde ela estiver definida

register = template.Library()

@register.filter(name='encode_id')
def encode_id_filter(value):
    return encode_id(value)