import os
import sys

from django.conf import settings

os.environ.get("DEBUG", "on") == "on"

SECRET_KEY = os.environ.get("SECRET_KEY", "uc5@4@-v6b59w5_-ct584_n7q53n!f+5hv-53c2x-ysz9qknds")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

settings.configure(
    DEBUG=True,
    SECRET_KEY="thisisthesecretkey",
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.http import HttpResponse, HttpResponseBadRequest
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django import froms

class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""
    height = forms.IntegerField(min_value=1, max_value=2000)
    width  = forms.IntegerField(min_value=1, max_value=2000)

def placeholder(request, width, height):
    form = ImageForm({'height': height, 'width': width})

    if form.is_valid():
        height = form.cleaned_data['height']
        width  = form.cleaned_data['width']
        # TODO: Generate image of requested size
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')
...
def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name="homepage")
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
