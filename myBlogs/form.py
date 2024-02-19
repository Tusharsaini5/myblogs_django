from.models import blog_category, blog_post
from django.forms import ModelForm
 


class Blog_Form(ModelForm):
    class Meta:
         model = blog_category
         fields = "__all__"

class BlogPost_Form(ModelForm):
     class Meta:
          Model= blog_post
          fields = "__all__"

          