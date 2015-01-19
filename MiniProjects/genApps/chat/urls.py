
from django.conf.urls import patterns, url


urlpatterns = patterns("chat.views",
    url("^oo/$", "rooms", name="rooms"),
    url("^icreate/$", "create", name="create"),
    url("^isystem_message/$", "system_message", name="system_message"),
    url("^i(?P<slug>.*)$", "room", name="room"),
)
