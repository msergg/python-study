from django.conf.urls import url
from products.views import detail, edit_comments


urlpatterns = [
    url(r'^detail/(?P<product_id>\d+)', detail),
    url(r'^edit/(?P<comment_id>\d+)', edit_comments),

]