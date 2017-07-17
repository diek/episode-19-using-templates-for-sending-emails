from django.conf.urls import include, url

urlpatterns = [
    url(r'^main/', include('main.urls', namespace='main')),
]
