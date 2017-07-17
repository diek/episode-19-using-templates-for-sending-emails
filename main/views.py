from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string


def email_txt(request):
    subject = "I am a text email"
    to = ['buddy@buddylindsey.com']
    from_email = 'test@example.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    body = render_to_string('main/email.txt', ctx)

    EmailMessage(subject=subject,
                 body=body,
                 from_email=from_email,
                 to=to).send()
    return HttpResponse('Plain Text Email Sent')


def email_html(request):
    """An alternate approach is to use:
    from django.core.mail import EmailMultiAlternatives
    https://docs.djangoproject.com/en/1.11/topics/email/#sending-alternative-content-types
    """

    subject = "I am an HTML email"
    to = ['buddy@buddylindsey.com']
    from_email = 'test@example.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    body = get_template('main/email.html').render(ctx)
    msg = EmailMessage(subject=subject,
                       body=body,
                       from_email=from_email,
                       to=to)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('HTML Email Sent')
