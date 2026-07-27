import os
from django.conf import settings
from django.http import FileResponse

def service_worker(request):
    path = os.path.join(settings.STATICFILES_DIRS[0], 'sw.js')
    response = FileResponse(open(path, 'rb'), content_type='application/javascript')
    response['Service-Worker-Allowed'] = '/'
    response['Cache-Control'] = 'no-cache'
    return response

def manifest(request):
    path = os.path.join(settings.STATICFILES_DIRS[0], 'manifest.json')
    return FileResponse(open(path, 'rb'), content_type='application/manifest+json')
