from django.contrib import admin # importing admin
from .models import Post, Comment # we import (include) the Post model as we want it to visible at admin page. (.) here means same directory,importing the Comment model

admin.site.register(Post) # To make our model visible on the admin page, we need to register the model with admin.site.register(Post)
admin.site.register(Comment) # To register the Comment model in the admin panel