# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

from django.conf import settings
from django.db import models # importing models
from django.utils import timezone # When time zone support is enabled (USE_TZ=True), Django uses time-zone-aware datetime objects. If your code creates datetime objects, they should be aware too.

class Post(models.Model): #defines our model(it is an object)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey – this is a link to another model.
    title = models.CharField(max_length=200) # models.CharField – this is how you define text with a limited number of characters.
    text = models.TextField() # models.TextField – this is for long text without a limit.
    created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField – this is a date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # method that publishes the post
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # __str__() we will get a text (string) with a Post title
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments') # The related_name option in models.ForeignKey allows us to have access to comments from within the Post model.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) # this is true/false field.

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

''' django.conf.settings - Will import settings object from django.conf package (Django's provided files) and abstracts the concepts of default settings and site-specific settings; it presents a single interface. It also decouples the code that uses settings from the location of your settings.

 on_delete=models.CASCADE - This is the behaviour to adopt when the referenced object is deleted. It is not specific to django, this is an SQL standard.CASCADE: When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.

 settings.AUTH_USER_MODEL returns only the string that is the name/path of the model.

 models.DateTimeField(blank=True, null=True) - null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types such as DateTimeField or ForeignKey will be stored as NULL in the DB.blank=True determines whether the field will be required in forms. This includes the admin and your own custom forms. If blank=True then the field will not be required, whereas if it's False the field cannot be blank.The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

 models.DateTimeField(default=timezone.now) then you're passing a callable to the model and it will be called each time a new instance is saved. With the parentheses, it's only being called once when models.py loads.

 A callable is an object allows you to use round parenthesis ( ) and eventually pass some parameters, just like functions.Every time you define a function python creates a callable object. In example, you could define the function func in these ways (it's the same):
 class a(object):def __call__(self, *args):print 'Hello'
 func = a()
 or ... 
def func(*args):print 'Hello'
You could use this method instead of methods like doit or run, I think it's just more clear to see obj() than obj.doit() '''