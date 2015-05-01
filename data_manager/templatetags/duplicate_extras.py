from django import template
import re
register = template.Library()

def titleize(s):
    return re.sub('[\W_]+', ' ', s.title())
    
def humanize(s):
    return re.sub('[\W_]+', ' ', s)
    
register.filter('titleize', titleize)
register.filter('humanize', humanize)