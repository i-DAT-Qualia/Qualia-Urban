from django import template
from django.template import RequestContext
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.inclusion_tag('components/dash_menu.html')
def show_menu(input, user):
    return {
        'input': input,
        'user': user
    }

@register.inclusion_tag('components/dash_filter.html')
def show_filters(filters, user):
    return {
        'filters': filters,
        'user': user
    }

@register.inclusion_tag('components/dash_time_filter.html')
def show_time_filters(filters, user):
    return {
        'filters': filters,
        'user': user
    }

@register.inclusion_tag('components/dashboard-circle.html')
def dash_circle(id, scale_string, data_string, number_string, percentage, trigger):
    return {
        'id': id,
        'scale_string': scale_string,
        'data_string': data_string,
        'number_string': number_string,
        'percentage': percentage,
        'trigger': trigger
    }

@register.inclusion_tag('components/dashboard-gauge.html')
def dash_gauge(data):
    return {
        'data': data,
    }

@register.inclusion_tag('components/colour.html')
def colour_code(code):
    options = {
        1:'00aff0',
        2:'4b78be',
        3:'915fa5',
        4:'912d91',
        5:'912d5f',
        6:'be235f',
        7:'f01923'
    }

    return {
        'colour_code': options[code],
    }

@register.filter(name='qr')
@stringfilter
def qr(value, args):
    '''
    Call <img src="{{ "url"|qr:"height"}}"> in template
    '''

    width=500

    if args:
        arg_list = [arg.strip() for arg in args.split(',')]
        if arg_list[0]:
            width = arg_list[0]

    height = width

    return 'https://chart.googleapis.com/chart?cht=qr&choe=UTF-8&chs='+ str(width)+ 'x' + str(height) +'&chl=' + value

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addplaceholder')
def addplaceholder(field, placeholder):
   return field.as_widget(attrs={"placeholder":placeholder})

@register.filter(name='addboot')
def addboot(field, placeholder):
   return field.as_widget(attrs={"class":"form-control","placeholder":placeholder})

@register.filter(name='addbootdate')
def addbootdate(field, placeholder):
   return field.as_widget(attrs={"class":"form-control datetimepicker","data-date-format":"YYYY-MM-DD HH:mm","placeholder":placeholder})
