# Generated by Django 3.1.7 on 2021-02-23 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='newTwinkleVisionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCategoryLayer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscatégories', to='NewTwinkleVision.newtwinklevisioncategory')),
            ],
            options={
                'verbose_name': 'Category Layer 2',
                'ordering': ('-date_updated',),
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCategoryLayer3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscatégories', to='NewTwinkleVision.newtwinklevisioncategorylayer2')),
            ],
            options={
                'verbose_name': 'Category Layer 3',
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCategoryLayer4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscatégories', to='NewTwinkleVision.newtwinklevisioncategorylayer3')),
            ],
            options={
                'verbose_name': 'Category Layer 4',
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCategoryLayer5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscatégories', to='NewTwinkleVision.newtwinklevisioncategorylayer4')),
            ],
            options={
                'verbose_name': 'Category Layer 5',
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCategoryLayer6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscatégories', to='NewTwinkleVision.newtwinklevisioncategorylayer5')),
            ],
            options={
                'verbose_name': 'Category Layer 6',
            },
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCsv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='newTwinkleVision/csvs/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='newTwinkleVisionCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=60, null=True, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='newTwinkleVisionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Payment Confirmed, Processing Order', 'Payment Confirmed, Processing Order'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncustomer')),
            ],
        ),
        migrations.CreateModel(
            name='newTwinkleVisionShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200, null=True)),
                ('suburb', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='newTwinkleVisionProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('specification', models.TextField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(blank=True, upload_to='newTwinkleVisionmain_product/')),
                ('image2', models.ImageField(blank=True, upload_to='newTwinkleVisionmain_product/')),
                ('image3', models.ImageField(blank=True, upload_to='newTwinkleVisionmain_product/')),
                ('image4', models.ImageField(blank=True, upload_to='newTwinkleVisionmain_product/')),
                ('stock', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategory')),
                ('categorylayer2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategorylayer2')),
                ('categorylayer3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategorylayer3')),
                ('categorylayer4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategorylayer4')),
                ('categorylayer5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategorylayer5')),
                ('categorylayer6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisioncategorylayer6')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='newTwinkleVisionOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisionorder')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisionproduct')),
            ],
        ),
        migrations.AddField(
            model_name='newtwinklevisioncustomer',
            name='shippingAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewTwinkleVision.newtwinklevisionshippingaddress'),
        ),
        migrations.AddField(
            model_name='newtwinklevisioncustomer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
