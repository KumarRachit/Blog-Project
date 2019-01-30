# A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template.Views are just Python functions.

from django.shortcuts import render 
''' In django render is used for loading the templates.So for this we
import-from django.shortcuts import render
its a template shortcut. Rendering is the process of gathering data (if any) and load the associated templates. '''

def post_list(request):
    return render(request, 'blog/post_list.html', {})
    #  we created a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.

''' Why does Django's render() function need the “request” argument?
The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.
A common template context processor is the auth context processor, which takes the request object, and adds the logged-in user to the context.
If you don't need to render the template with a request context, you can use request=None.
def my_view(request):
    return render(None, "my_template.html", {'foo': 'bar'}) '''

# In django, template is rendered to HTTPResponse. ie the template is interpreted and translated to appropriate output. In django templates can be rendered to http response (render_to_response) or string (render_to_string).
