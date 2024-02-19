from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog_category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    blogcat_description=models.TextField(max_length=200)
    def __str__(self):
        return self.blog_cat
    # (self):
    #     return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)
    def __str__(self):
        return self.u_email
    
class blog_post(models.Model):
    blog_title = models.CharField(max_length=80)
    blog_img = models.ImageField(upload_to='images/')
    blog_description=RichTextField()
    Blog_cat = models.ForeignKey(blog_category,null=True, default= None ,on_delete=models.CASCADE)
    like_count =models.IntegerField(default=0, null = True)
    view_count = models.IntegerField(default=0, null = True)
    def __str__(self):
        return self.blog_title
    
class comment(models.Model):
    comment_email = models.EmailField(max_length=100)
    comment_info = models.CharField(max_length=100)
    comment_id = models.ForeignKey(blog_post,null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_email
    
    