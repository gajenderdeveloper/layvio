from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,logout, login
from django.shortcuts import render,redirect,reverse
from .models import *
from django.db.models import Count
from django.contrib import messages
import os
from django.http import FileResponse
from .forms import UserCreationForm, UserLoginForm
from .encrypt_decrypt import encrypt_id, decrypt_id
# Create your views here.

def home(request):
    
    return render(request, 'index.html', {
     
        
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
    if url_name == 'free-templates':
        template_type = 'free'
    else:
        template_type = 'premium'


    if industry_slug:
        templates = Template.objects.filter(template_type=template_type,status=True,industry__slug=industry_slug)
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
        'template_type':template_type
        
    });
def primeproduct(request):
    templates = Template.objects.filter(template_type='premium',status=True)
    industries = Industry.objects.filter(status=True)
    return render(request, 'prime-product.html', {
        'templates': templates,
        'industries': industries
        
    });

def readymadesolutions(request):
    industries = Industry.objects.filter(status=True)
    return render(request, 'readymade-solutions.html', {
        'industries': industries
        
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

