# A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template.Views are just Python functions. views are supposed to do: connect models and templates. In our post_list view we will need to take the models we want to display and pass them to the template. In a view we decide what (model) will be displayed in a template.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404 # Importing render function and 404 error
from .models import Post
from django.utils import timezone
from .forms import PostForm # Importing our 'form whose name i.e PostForm' from 'forms.py'

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
  return render(request, 'blog/post_list.html', {'posts': posts})
    # We want published blog posts sorted by published_date.Variable for our QuerySet: 'posts'. Treat this as the name of our QuerySet. 

    #  we created a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.In the render function we have one parameter request (everything we receive from the user via the Internet) and another giving the template file ('blog/post_list.html'). The last parameter, {}, is a place in which we can add some things for the template to use. We need to give them names (we will stick to 'posts' right now). :) It should look like this: {'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes: ''.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST) # we want to construct the PostForm with data from the form.

    # The next thing is to check if the form is correct (all required fields are set and no incorrect values have been submitted). We do that with form.is_valid().

    if form.is_valid():
      post = form.save(commit=False) # we save the form with 'form.save'.'commit=False' means that we don't want to save the Post model yet – we want to add the author first.
      post.author = request.user # we add an author (since there was no author field in the PostForm and this field is required).
      # post.published_date = timezone.now() New posts will be saved as drafts that we can review later on rather than being instantly published.Currently when we're creating new posts using our New post form the post is published directly. To instead save the post as a draft, remove this line.
      post.save() # post.save() will preserve changes (adding the author) and a new blog post is created!
      return redirect('post_detail', pk=post.pk) # "Go to the post_detail page for the newly created post".post_detail is the name of the view we want to go to. Remember that this view requires a pk variable? To pass it to the views, we use pk=post.pk, where post is the newly created blog post!
  else:
        form = PostForm() # # To create a new Post form, we need to call PostForm() and pass it to the template. 
        return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts}) # The line posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') makes sure that we take only unpublished posts (published_date__isnull=True) and order them by created_date (order_by('created_date')).

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list') # After deleting a post we want to go to the webpage with a list of posts, so we are using redirect.

''' Why does Django's render() function need the “request” argument?
The render() shortcut renders templates with a request context. Template context processors take the request object and return a dictionary which is added to the context.
A common template context processor is the auth context processor, which takes the request object, and adds the logged-in user to the context.
If you don't need to render the template with a request context, you can use request=None.
def my_view(request):
    return render(None, "my_template.html", {'foo': 'bar'}) '''

# In django, template is rendered to HTTPResponse. ie the template is interpreted and translated to appropriate output. In django templates can be rendered to http response (render_to_response) or string (render_to_string).

''' In django render is used for loading the templates.So for this we
import-from django.shortcuts import render
its a template shortcut. Rendering is the process of gathering data (if any) and load the associated templates. '''

''' This time our view is given an extra parameter, pk. Our view needs to catch it, right? So we will define our function as def post_detail(request, pk):

we want to get one and only one blog post. To do this, we can use querysets, like this:
Post.objects.get(pk=pk)

In case there is no Post with the given pk, django will display much nicer page, the Page Not Found 404 page.

In blog/urls.py we created a URL rule named post_detail that refers to a view called views.post_detail. This means that Django will be expecting a view function called post_detail inside blog/views.py. '''

''' Most of the time you will use form.save() without commit=False, but in this case, we need to supply it.  '''

''' Page redirection is needed for many reasons in web application. You might want to redirect a user to another page when a specific action occurs, or basically in case of error.In Django, redirection is accomplished using the 'redirect' method. '''