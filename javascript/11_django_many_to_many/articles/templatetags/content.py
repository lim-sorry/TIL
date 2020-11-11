from django import template
from django.utils.safestring import mark_safe
from ..models import Hashtag
from django.urls import reverse

register = template.Library()

@register.filter(needs_autoescape=True)
def link_hashtag(content, autoescape=True):
    linked_content = ''
    for word in content.split():
        if word.startswith('#'):
            hashtag = Hashtag.objects.get(content=word)
            url = reverse('articles:hashtag', kwargs={'hashtag_pk':hashtag.pk})
            linked_content += f' <a href="{url}">{word}</a> '
        else:
            linked_content += word
    return mark_safe(linked_content)