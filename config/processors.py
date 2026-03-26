from core.forms import ContactUsForm


def contact(request):
    form = ContactUsForm

    return {
        "form": form,
    }
