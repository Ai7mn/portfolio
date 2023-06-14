from django import forms

from projects.models import ContactUs


class ContactUsForm(forms.ModelForm):
    sender_name = forms.CharField(
        error_messages={'required': 'This Field is Required'},
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    sender_email = forms.EmailField(
        error_messages={'required': 'This Field is Required'},
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        error_messages={'required': 'This Field is Required'},
        widget=forms.Textarea(attrs={'rows': '5', 'placeholder': 'Your Message'})
    )

    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})
