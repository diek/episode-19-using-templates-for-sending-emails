from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='home'),
    url(r'^email_one/$', views.email_txt, name='email_txt'),
    url(r'^email_two/$', views.email_html, name='email_html'),
]
