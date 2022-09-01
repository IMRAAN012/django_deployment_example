from django import template
register = template.Library() # Here Library should be capital 'L'

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string:
    """
    return value.replace(arg,'')
register.filter('cut',cut)


@register.filter(name = 'cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string:
    """
    return value.replace(arg,'')


@register.filter(name = 'capfirst')
def capfirst(value,arg):
    """
    This cuts out all values of "arg" from the string:
    """
    return value.replace(arg,'')

@register.filter(name = 'first')
def first(value,arg):
    """
    This cuts out all values of "arg" from the string:
    """
    return value.replace(arg,'')

@register.filter(name = 'join')
def join(value,arg):
    """
    This cuts out all values of "arg" from the string:
    """
    return value.replace(arg,'')
