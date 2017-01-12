from django.conf.urls import url
from products.views import detail


urlpatterns = [
    url(r'^detail/(?P<product_id>\d+)', detail)

]