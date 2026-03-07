from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,logout, login
from django.shortcuts import render,redirect,reverse
from .models import *
from django.db.models import Count
from django.contrib import messages
import os
from django.http import FileResponse,HttpResponse
import json

from .forms import UserCreationForm, UserLoginForm
from .encrypt_decrypt import encrypt_id, decrypt_id
# Create your views here.

def home(request):
    
    industries = Industry.objects.filter(status=True)

    templates_free = Template.objects.filter(template_type='free',status=True).order_by('-id')[:6]
    templates_paid = Template.objects.filter(template_type='premium',status=True).order_by('-id')[:6]

    return render(request, 'index.html', {
        'industries': industries,
        'templates_free':templates_free,
        'templates_paid':templates_paid
        
    });
def all_industries(request):
    
    # inducstry with sub industry
    industries = Industry.objects.filter(status=True)


    return render(request, 'all-industries.html', {
        'industries': industries
        
    });

def freetemplates(request,industry_slug=None):
    # get url name
    url_name = request.resolver_match.url_name
    print(url_name)

    if url_name == 'bootstrap4':
        template_text = 'Bootstrap 4'
        template_type = 'Bootstrap 4'
    elif url_name == 'bootstrap5':
        template_text = 'Boostrap 5'
        template_type = 'Boostrap 5'

    elif url_name == 'free-templates':
        template_type = 'free'
        template_text = 'Free Templates'
    else:
        template_type = 'premium'
        template_text = 'Prime Products'


    if industry_slug:
        templates = Template.objects.filter(template_type=template_type,status=True,industry__slug=industry_slug)
    else:
        if url_name in ['bootstrap4','bootstrap5']:
            templates = Template.objects.filter(html_type__icontains=template_type, status=True)
        else:

            templates = Template.objects.filter(template_type=template_type,status=True)
    


    industries = Industry.objects.filter(status=True)
    
    # pagging code
    page = request.GET.get('page', 1)
    paginator = Paginator(templates, 10)
    try:
        templates = paginator.page(page)
    except PageNotAnInteger:
        templates = paginator.page(1)
    except EmptyPage:
        templates = paginator.page(paginator.num_pages)
        # end of pagging code
    return render(request, 'free-templates.html', {
        'templates': templates,
        'industries': industries,
        'industry_slug':industry_slug,
        'template_type':template_type,
        'template_text':template_text
        
    });
def primeproduct(request):
    templates = Template.objects.filter(template_type='premium',status=True)
    industries = Industry.objects.filter(status=True)
    return render(request, 'prime-product.html', {
        'templates': templates,
        'industries': industries
        
    });

def readymadesolutions(request):
    #industries = Industry.objects.filter(status=True)
    templates = Readimate_Solution.objects.filter(status=True)
    realWebsite = RealWebsite.objects.filter(status=True)
    return render(request, 'readymade-solutions.html', {
        #'industries': industries,
        'templates': templates,
        'realWebsite':realWebsite
        
    });

def readymadeall(request):
    industries = Industry.objects.filter(status=True)
    templates = Readimate_Solution.objects.filter(status=True)
    return render(request, 'readimate_all.html', {
        'industries': industries,
        'templates': templates
        
    });

def readymade_detail(request,template_slug):
    template_detail = Readimate_Solution.objects.get(slug=template_slug)
    template_id = str(template_detail.id)+'&&'+str(template_detail.name)

    template_id = encrypt_id(template_id)  # For URL
    # print(encrypted_id)
    # decrypted_id = decrypt_id(encrypted_id)  # When processing
    # print(decrypted_id)
    print("===========")
    print(template_detail.name)
    
    return render(request, 'readymade_detail.html', {
     'template_detail' : template_detail,
     'template_id' : template_id
        
    });

def showcase(request):
    industries = Industry.objects.filter(status=True)
    realWebsite = RealWebsite.objects.filter(status=True)
    return render(request, 'showcase.html', {
        'industries': industries,
        'templates': realWebsite
        
    });


def Signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            print("else errorrr")
            messages.error(request, "Invalid information.")
    else:
        print("else================")
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
    

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')  # Default redirect
           
        else:
            form = UserLoginForm()
            messages.error(request, "Invalid information.")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {
        'form': form
    });

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):

    downloads = Download.objects.filter(user_id=request.user.id)

    return render(request, 'profile.html', {
        'downloads':downloads,
        
     
        
    });
def template_detail(request,template_slug):
    template_detail = Template.objects.get(slug=template_slug)
    template_id = str(template_detail.id)+'&&'+str(template_detail.name)

    template_id = encrypt_id(template_id)  # For URL
    # print(encrypted_id)
    # decrypted_id = decrypt_id(encrypted_id)  # When processing
    # print(decrypted_id)
    
    return render(request, 'template_detail.html', {
     'template_detail' : template_detail,
     'template_id' : template_id
        
    });
def template_download(request,template_name):
    decrypted_id = decrypt_id(template_name)
    template_id = decrypted_id.split('&&')[0]
    print(template_id)

    template_detail = Template.objects.get(id=template_id)
    # check user is logged in or not
    if not request.user.is_authenticated:
        #return redirect('login')
        #return redirect(reverse('login', kwargs={'next': 'template/'+template_detail.slug}))
        return redirect('/login?next=template/' + template_detail.slug)
    # get template detail
   
    file_path = template_detail.upload_file.path
    file_name = template_detail.upload_file.name
    print(file_path)
    print(file_name)
    if os.path.exists(file_path):
        
        download_obj = Download()
        download_obj.template_id = template_detail
        download_obj.user_id = User.objects.get(id=request.user.id)
        download_obj.template_id_str = encrypt_id(str(template_id)+'&&'+str(template_detail.name))
        download_obj.save()

        response = FileResponse(open(file_path, 'rb'))
        response['Content-Type'] = 'application/zip'
        response['Content-Disposition'] = 'attachment; filename="yourfile.zip"'
        return response
    # send file to user
    return redirect('home')






########foter view
def bootstrap4(request):
    return render(request, 'bootstrap4.html', {
           
    });
def bootstrap5(request):
    return render(request, 'bootstrap5.html', {
           
    });
def code_snippets(request):
    return render(request, 'code_snippets.html', {
           
    });
def blog(request):
    return render(request, 'blog.html', {   
    });
def membership(request):
    return render(request, 'membership.html', {   
    });
def buy_hosting(request):
    return render(request, 'buy_hosting.html', {   
    });
def domain_for_sale(request):
    return render(request, 'domain_for_sale.html', {   
    });
def request_template(request):
    return render(request, 'request_template.html', {   
    });

def start_selling(request):
    return render(request, 'start_selling.html', {   
    });

def about_us(request):
    return render(request, 'about_us.html', {   
    });
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        #phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_obj = ContactUs()
        contact_obj.name = name
        contact_obj.email = email
        contact_obj.type = ''
        contact_obj.message = message
        contact_obj.save()
        messages.success(request, "Thank you for contacting us. We will get back to you soon.")
    return render(request, 'contact_us.html', {   
    });
def custom_work(request):
    if request.method == 'POST':
        email = request.POST.get('email')   
        message = request.POST.get('message')
        plan = request.POST.get('plan')
        budget = request.POST.get('budget')
        customWork_obj = CustomWork()
        customWork_obj.email = email
        customWork_obj.message = message
        customWork_obj.plan = plan
        customWork_obj.budget = budget
        customWork_obj.save()
        messages.success(request, "Thank you for contacting us. We will get back to you soon.")
    


    return render(request, 'custom_work.html', {   
    });
def license(request):
    return render(request, 'license.html', {   
    });
def advertise(request):
    return render(request, 'advertise.html', {   
    });
def affiliate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        affiliate_obj = Affiliate()
        affiliate_obj.name = name
        affiliate_obj.email = email
        affiliate_obj.website = website
        affiliate_obj.message = message
        affiliate_obj.save()
        messages.success(request, "Thank you for submitting your request. We will get back to you soon.")


    return render(request, 'affiliate.html', {   
    });

def faqs(request):
    return render(request, 'faqs.html', {   
    });

def free_support(request):
    return render(request, 'free_support.html', {   
    });

def term_and_condition(request):
    return render(request, 'term_and_condition.html', {   
    });

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {   
    });

def refund_policy(request):
    return render(request, 'refund_policy.html', {   
    });

def guest_purchase(request):
    return render(request, 'guest_purchase.html', {   
    });
def price(request):
    return render(request, 'price.html', {   
    });


def getSubIndustry(request):
    id = request.GET.get('id', '')
    result = list(SubIndustry.objects.filter(industry_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
