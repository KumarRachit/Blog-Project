from django import forms # Import Django forms first 
from .models import Post, Comment # Import Post & Comment model

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('author', 'text',)

''' 'PostForm' is the name of our form.form created from forms.'ModelForm' will be automatically created and then can later be tweaked by you.If your form is going to be used to directly add or edit a Django model, you can use a ModelForm to avoid duplicating your model description.ModelForm is a class which enables you to write Forms which are closely coupled with a Model. You can inherit this class, associate it with a Model and then render it in templates as any other HTML form (ModelForms render Model fields as HTML form elements).

Why is it useful?

It could be a huge list, however I would write only some of the important points:
ModelForm creates the form elements using the Model field definitions. This saves your time, efforts and some lines of code which you would have written to create the form field elements.

By default all the validations/constraints applied on the Model fields are also applied on ModelForms and so you do not need to put separate server side validations for these forms.

You can save the data submitted through ModelForm directly into the database using the ModelForm instances. '''

'''  class Meta, where we tell Django which model should be used to create this form (model = Post).

Which field(s) should end up in our form. In this scenario we want only title and text to be exposed – author should be the person who is currently logged in (you!) and created_date should be automatically set when we create a post(i.e. in the code).  '''