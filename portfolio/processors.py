from math import ceil

from django.conf import settings
import re
from projects.forms import ContactUsForm


def contact(request):
    form = ContactUsForm

    return {'form': form, }
