# we're importing Django's function path and all of our views from the blog application
from django.urls import path # path() Function Returns an element for inclusion in urlpatterns with 4 args: Two required route and view and two are optional kwargs and name path(route, view, kwargs=None, name=None)
from . import views # Importing views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

''' As you can see, we're now assigning a view called post_list to the root URL. This URL pattern will match an empty string and the Django URL resolver will ignore the domain name (i.e., http://127.0.0.1:8000/) that prefixes the full url path. This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.

The last part, name='post_list', is the name of the URL that will be used to identify the view. This can be the same as the name of the view but it can also be something completely different. We will be using the named URLs later in the project, so it is important to name each URL in the app. We should also try to keep the names of URLs unique and easy to remember. '''