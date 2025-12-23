from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.text import slugify 
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_file_extension,validate_file_extension_zip


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    first_name =models.CharField(max_length=250,null=True, blank=True)
    last_name =models.CharField(max_length=250,null=True, blank=True)
    email = models.EmailField('Email', max_length=40,null=False, blank=False,unique=True) 
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Add any other required fields here

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Users"



class StaticPages(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    slug = models.SlugField(unique=True,max_length=600)
    description = RichTextField(blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        :return: the Category name
        """
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(StaticPages, self).save(*args, **kwargs)

    class Meta:
        """docstring for meta"""
        ordering = ('id',)
        verbose_name_plural = "Static Pages"



class Industry(models.Model):
    name = models.CharField('Industry Name', max_length=40, unique=True)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to='',validators=[validate_file_extension])
    status = models.BooleanField(default=True)
    show_home = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        :return: the Industry name
        """
        return self.name

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Industries"


# -------------------------Sub Category Management-----------------------------


class SubIndustry(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry')
    name = models.CharField('SubCategory Name', max_length=40, unique=True)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        :return: the SubCategory name
        """
        return self.name

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Sub Industries"


class Template(models.Model):

    industry    = models.ForeignKey(Industry, on_delete=models.CASCADE)
    sub_industry = models.ForeignKey(SubIndustry, on_delete=models.CASCADE)
    name = models.CharField('Template Name', max_length=40, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='',validators=[validate_file_extension])
    
    short_description = models.TextField(max_length=200)


    template_type = models.CharField(max_length=20, choices=[('free', 'Free'), ('premium', 'Premium')])

    price = models.IntegerField(default=0,blank=False,null=False)

    
    upload_file = models.FileField('upload html/zip file',upload_to='upload_html_files/',validators=[validate_file_extension_zip])

    
    template_details = RichTextUploadingField(blank=True)
    details_image = models.ImageField(upload_to='', default='website.jpg',validators=[validate_file_extension],blank=True)
    releadse_on = models.DateTimeField(null=True, blank=True)
    html_type = models.CharField(max_length=40,null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    theme_version = models.CharField(max_length=40,null=True, blank=True)
    review_count = models.IntegerField(default=0,null=True, blank=True)
    item_code    = models.CharField(max_length=40,null=True, blank=True)
    file_include = models.CharField(max_length=200,null=True, blank=True)
    browsers = models.CharField(max_length=200,null=True, blank=True)
  
    status = models.BooleanField( default=True)
  
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        :return: the template name
        """
        return str(self.name) if self.name else "-"

     
class Download(models.Model):
    template_id = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='template')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    template_id_str = models.CharField(max_length=200,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        :return: the template name
        """
        return str(self.template_id)
    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Download Template"