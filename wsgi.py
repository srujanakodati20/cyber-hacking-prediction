import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cyber_Hacking_Breaches.settings")

application = get_wsgi_application()
