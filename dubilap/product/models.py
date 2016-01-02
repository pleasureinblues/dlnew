from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
import os
import datetime
from django.core.validators import RegexValidator

# Create your models here.

### STORAGE ###

pi = FileSystemStorage(location='/media/product_images')
ci = FileSystemStorage(location='/media/category_icons')

### FILE / IMAGE UPLOAD FUNCTIONS ###

def update_Product_image_filename(instance, filename):
    ctime = datetime.datetime.now()
    ctime_string = ctime.strftime("%Y%m%d%H%M%S")
    path = "product_images"
    basename , extension = os.path.splitext(filename)
    format = "dubailap_" + ctime_string + extension
    return os.path.join(path, format)


def update_cat_icon_filename(instance, filename):
    ctime = datetime.datetime.now()
    ctime_string = ctime.strftime("%Y%m%d%H%M%S")
    path = "category_icons"
    basename , extension = os.path.splitext(filename)
    format = "cat_icon_" + ctime_string + extension
    return os.path.join(path, format)


def update_brand_icon_filename(instance, filename):
    ctime = datetime.datetime.now()
    ctime_string = ctime.strftime("%Y%m%d%H%M%S")
    path = "brand_icons"
    basename , extension = os.path.splitext(filename)
    format = "brand_icon_" + ctime_string + extension
    return os.path.join(path, format)


### MODELS ###

class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category_icon = models.ImageField(upload_to=update_cat_icon_filename)

        # Override th __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


class Brand(models.Model):
    brand_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    brand_icon = models.ImageField(upload_to=update_brand_icon_filename)

        # Override th __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)



class ProductProfile(models.Model):
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    product_name = models.CharField(max_length=128)
    model_name = models.CharField(max_length=128)
    generation = models.CharField(max_length=128)
    processor = models.CharField(max_length=128)
    ram = models.DecimalField(max_digits=2, decimal_places=0)
    hdd = models.DecimalField(max_digits=6, decimal_places=2)
    optical_drive = models.CharField(max_length=128)
    display = models.CharField(max_length=128)
    card_reader = models.CharField(max_length=128)
    blue_tooth = models.CharField(max_length=128)
    web_cam = models.CharField(max_length=128)
    warranty = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    condition = models.TextField()
    product_image = models.ImageField(upload_to=update_Product_image_filename)
    post_date = models.DateTimeField(db_index=True, auto_now_add=True)

    # Override th __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.product_name



class UserProfile(models.Model):
    # This line is required.Links Userprofile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override th __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



class Customer_ps_contact(models.Model):
    name = models.CharField(max_length=128, help_text="Name")
    email = models.EmailField(max_length=75, help_text="Email")
    subject = models.CharField(max_length=128,help_text="Subject" )
    product = models.ForeignKey(ProductProfile, help_text="Product")
    message = models.TextField(help_text="Message")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, help_text="Phone Number") # validators should be a list

    def __unicode__(self):
        return self.name
