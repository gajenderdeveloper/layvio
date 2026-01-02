from django.contrib import admin
from django.urls import re_path as url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', include('django.contrib.auth.urls')),
    url(r'^$', views.home, name='home'),
    path('all-industries', views.all_industries, name='all_industries'),
    path('free-templates', views.freetemplates, name='free-templates'),
    path('free-templates/<industry_slug>', views.freetemplates, name='free-templates'),

    path('prime-product', views.freetemplates, name='prime-product'),
    path('prime-product/<industry_slug>', views.freetemplates, name='prime-product'),

    path('readymade-solutions', views.readymadesolutions, name='readymade-solutions'),

    path('signup', views.Signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('template/<template_slug>', views.template_detail, name='template_detail'),
    path('template/download/<template_name>', views.template_download, name='template_download'),

    ### footer link ###########
    path('bootstrap-4', views.bootstrap4, name='bootstrap4'),
    path('bootstrap-5', views.bootstrap5, name='bootstrap5'),
    path('code-snippets', views.code_snippets, name='code_snippets'),
    path('blog', views.blog, name='blog'),
    path('membership', views.membership, name='membership'),
    path('buy-hosting', views.buy_hosting, name='buy_hosting'),
    path('domain-for-sale', views.domain_for_sale, name='domain_for_sale'),
    path('request-template', views.request_template, name='request_template'),
    path('start-selling', views.start_selling, name='start_selling'),
    path('about-us', views.about_us, name='about_us'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('custom-work', views.custom_work, name='custom_work'),
    path('license', views.license, name='license'),
    path('advertise', views.advertise, name='advertise'),
    path('affiliate', views.affiliate, name='affiliate'),

    path('faqs', views.faqs, name='faqs'),
    path('free-support', views.free_support, name='free_support'),
    path('term-and-condition', views.term_and_condition, name='term_and_condition'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('refund-policy', views.refund_policy, name='refund_policy'),
    path('guest-purchase', views.guest_purchase, name='guest_purchase'),



]

urlpatterns += [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]