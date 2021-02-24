from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Count
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
class opticalLensLabCustomer(models.Model):
    User            = settings.AUTH_USER_MODEL
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    shippingAddress = models.ForeignKey('opticalLensLabShippingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    email 			= models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)

    def __str__(self):
        if self.email:
            return self.email
    @property
    def orders(self):
        order_count = self.opticallenslaborder_set.all().count()
        return str(order_count)




    # Create your models here.

class opticalLensLabCsv(models.Model):
    file_name = models.FileField(upload_to='opticalLensLabcsvs/')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File ID: {self.id} "


class opticalLensLabProduct(models.Model):
    name                = models.CharField(max_length=200, null=False)
    sku                 = models.CharField(max_length=200, null=False)
    description         = models.TextField(max_length=2000, null=False)
    specification       = models.TextField(max_length=2000, null=False)
    price               = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image1              = models.ImageField(upload_to='opticalLensLabmain_product/', blank=True, null=False)
    image2              = models.ImageField(upload_to='opticalLensLabmain_product/', blank=True, null=False)
    image3              = models.ImageField(upload_to='opticalLensLabmain_product/', blank=True, null=False)
    image4              = models.ImageField(upload_to='opticalLensLabmain_product/', blank=True, null=False)
    category            = models.ForeignKey('opticalLensLabCategory' , on_delete=models.SET_NULL, blank=True, null=True)
    categorylayer2      = models.ForeignKey('opticalLensLabCategoryLayer2' , on_delete=models.SET_NULL, blank=True, null=True)
    categorylayer3      = models.ForeignKey('opticalLensLabCategoryLayer3' , on_delete=models.SET_NULL, blank=True, null=True)
    categorylayer4      = models.ForeignKey('opticalLensLabCategoryLayer4' , on_delete=models.SET_NULL, blank=True, null=True)
    categorylayer5      = models.ForeignKey('opticalLensLabCategoryLayer5' , on_delete=models.SET_NULL, blank=True, null=True)
    categorylayer6      = models.ForeignKey('opticalLensLabCategoryLayer6' , on_delete=models.SET_NULL, blank=True, null=True)
    stock               = models.IntegerField(null=False)
    tags                = TaggableManager()
    def __str__(self):
        return self.name

    @property
    def imageURL1(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    def imageURL2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url
    def imageURL3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url
    def imageURL4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url

class opticalLensLabOrder(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Payment Confirmed, Processing Order', 'Payment Confirmed, Processing Order'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        )
    customer = models.ForeignKey(opticalLensLabCustomer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer)

    @property
    def shipping(self):
        shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.opticallenslaborderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.opticallenslaborderitem_set.all()
        allitems = sum([item.quantity for item in orderitems])
        return allitems

class opticalLensLabOrderItem(models.Model):
    product = models.ForeignKey(opticalLensLabProduct, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(opticalLensLabOrder, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class opticalLensLabShippingAddress(models.Model):
    country = models.CharField(max_length=200, null=False)
    address1 = models.CharField(max_length=200, null=False)
    address2 = models.CharField(max_length=200, null=True)
    suburb = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=False)
    province = models.CharField(max_length=200, null=False)
    postal_code = models.CharField(max_length=20, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.country)


class opticalLensLabCategory(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True, max_length=150, unique=True, db_index=True)

    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategory , self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_added', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name




class opticalLensLabCategoryLayer2(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True)
    category            = models.ForeignKey('opticalLensLabCategory', related_name='souscatégories', on_delete=models.SET_NULL, blank=True, null=True)

    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategoryLayer2 , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category Layer 2'
        ordering = ('-date_updated', )


    def __str__(self):
        return self.category_name





class opticalLensLabCategoryLayer3(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True)
    category            = models.ForeignKey('opticalLensLabCategoryLayer2', related_name='souscatégories', on_delete=models.SET_NULL, blank=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)


    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategoryLayer3 , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category Layer 3'

    def __str__(self):
        return self.category_name




class opticalLensLabCategoryLayer4(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True)
    category            = models.ForeignKey('opticalLensLabCategoryLayer3', related_name='souscatégories', on_delete=models.SET_NULL, blank=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategoryLayer4 , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category Layer 4'

    def __str__(self):
        return self.category_name




class opticalLensLabCategoryLayer5(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True)
    category            = models.ForeignKey('opticalLensLabCategoryLayer4', related_name='souscatégories', on_delete=models.SET_NULL, blank=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategoryLayer5 , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category Layer 5'

    def __str__(self):
        return self.category_name




class opticalLensLabCategoryLayer6(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True)
    category            = models.ForeignKey('opticalLensLabCategoryLayer5', related_name='souscatégories', on_delete=models.SET_NULL, blank=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(opticalLensLabCategoryLayer6 , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category Layer 6'


    def __str__(self):
        return self.category_name
