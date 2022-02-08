from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name + " ",self.time) 
    
    # def get_absolute_url(self):
    #     return reverse("blog_detail", kwargs={"pk": self.pk})

    # class Meta:
    #     verbose_name = _("blog")
    #     verbose_name_plural = _("blogs")

    

    
