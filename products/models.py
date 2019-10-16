import random,os

from django.db import models
from django.db.models import Q
# Create your models here.
#util method for file upload
from django.urls import reverse

from .utils import unique_slug_gen
from django.db.models.signals import pre_save




def get_fine_name(filepath):
    base_name = os.path.basename(filepath)
    #print(base_name)
    new,ext = os.path.splitext(base_name)
    #print(new,ext)
    return new,ext
def upload_image(image_object, filename):
    #print(image_object)
    #print(filename)
    new_imag_name = random.randint(1,32345435)
    new,ext = get_fine_name(filename)
    final_filename = '{new_imag_name}{ext}'.format(new_imag_name=new_imag_name,ext=ext)

    return 'products/{new_image_name}/{final_filename}'.format(new_image_name=new_imag_name,final_filename=final_filename)



#Featured querysets or our own custom query set.
#Customizing queryset
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)
    def featured(self):
        return self.filter(featured=True,active=True)
    def search(self,query):
        lookups = Q(product_name__icontains=query)|Q(description__icontains=query)|Q(price__icontains=query)
        return self.filter(lookups).distinct()

#extyendeing model
class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def all(self):
        #return self.get_queryset().active()
        return self.get_queryset().all()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            print(qs.first())
            return qs.first()
        return None
    def search(self,query):
        return self.get_queryset().active().search(query)




class Product(models.Model):

    product_name = models.CharField(max_length=120)
    slug         = models.SlugField(blank=True,unique=True)
    description  = models.TextField(max_length=250)
    price        = models.DecimalField(default=0.00,decimal_places=2,max_digits=30)
    image        = models.ImageField(upload_to=upload_image,null=True,blank=False)
    featured     = models.BooleanField(default=False)
    active       = models.BooleanField(default=True)
    objects = ProductManager()

    def get_absolute_url(self):
        #return '/products/{slug}/'.format(slug=self.slug)
        return reverse('slug_view',kwargs={'slug': self.slug})

    def __str__(self):
        return self.product_name

    def __unicode__(self):
        return self.product_name



#pre_save is used save the values before save the Model data
def product_pre_save_reciver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_gen.unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciver,sender=Product)

