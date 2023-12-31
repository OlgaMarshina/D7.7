from django import template

register = template.Library()
list_ = ['Конкурс', 'Флаг', 'Массаж', 'Стресс']


@register.filter()
def censor(text):
    correction = text
    for bad_word in list_:
        correction = correction.replace(bad_word.lower(), bad_word[:1] + '*' * (len(bad_word) - 1))
    correction = correction.lower()


    return correction