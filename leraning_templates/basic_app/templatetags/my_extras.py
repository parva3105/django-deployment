from django import template

register  = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    # This Cuts out all value of arg from the string
    return vaule.replace(arg,'')



# register.filter('cut',cut)

