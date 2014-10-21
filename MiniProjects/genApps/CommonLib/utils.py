#################################
# name : utils.py
# target : store all util functions
#################################
def get_client_ip(request):
    """ return IP address for a request in a string format  """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
