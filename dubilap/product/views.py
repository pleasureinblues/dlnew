from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from product.forms import Customer_ps_contactForm
from product.models import ProductProfile, Category, Brand


# Create your views here.


def home(request):
    products = ProductProfile.objects.all()
    context_dict = {'products': products}
    response = render(request,'home.html', context_dict)
    return response

def index (request):
    context_dict = {}
    context_dict['abc'] = 'We are here'
    return render(request, 'product/index.html', context_dict)


def about (request):
    context_dict = {}
    context_dict['abc'] = 'We are here'
    return render(request, 'product/about.html', context_dict)


def contact (request):
    context_dict = {}
    context_dict['abc'] = 'We are here'
    return render(request, 'product/contact.html', context_dict)

#####################
# CUSTOMER CONTACT
#####################

def mail_customer_contact(name, email, subject,message,send_a_copy):
    subject = "Customer Contact @ Dubilap: " + subject
    message = "Dear Admin"+"\n\n\n"+"Following message has been received from '" + name + "' having email address: "+email+":\n\n"+message
    if send_a_copy:
        send_mail(subject,
                  message,
                  'enquriy.dubailap@gmail.com',
                  ['pleasureinblues@gmail.com', email],
                  fail_silently=False)
    else:
        send_mail(subject,
          message,
          'enquriy.dubailap@gmail.com',
          ['pleasureinblues@gmail.com'],
          fail_silently=False)


def contact_us (request):
    context_dict = {}
    context_dict['abc'] = 'We are here'
    if request.POST:  # If this is true, the view received POST
        form_data_dict = request.POST
        name = form_data_dict['name']
        email = form_data_dict['email']
        subject = form_data_dict['subject']
        message = form_data_dict['message']
        send_a_copy = form_data_dict.get('send_a_copy', False)

        print (name)
        print (email)
        print (subject)
        print (message)
        print (send_a_copy)
        mail_customer_contact(name,email,subject,message,send_a_copy)
    return render(request, 'product/contact.html', context_dict)

###################################




def product_page(request, product_id):
    product = ProductProfile.objects.get(pk=product_id)
    context_dict = {'product': product}
    response = render(request,'product/product_page.html', context_dict)
    return response


def categories(request):
    category = Category.objects.all()
    context_dict = {'cat': category}
    response = render(request,'product/categories.html', context_dict)
    return response


def category_page(request, cat_name_slug):
    cat = Category.objects.get(slug=cat_name_slug)
    context_dict = {}
    products = ProductProfile.objects.filter(category=cat)
    context_dict['category'] = cat
    context_dict['products'] = products
    response = render(request,'product/category_page.html', context_dict)
    return response



def brands(request):
    brands = Brand.objects.all()
    context_dict = {'brands': brands}
    response = render(request,'product/brands.html', context_dict)
    return response


def brand_page(request, brand_name_slug):
    brand = Brand.objects.get(slug=brand_name_slug)
    context_dict = {}
    products = ProductProfile.objects.filter(brand=brand)
    context_dict['brand'] = brand
    context_dict['products'] = products
    response = render(request,'product/brand_page.html', context_dict)
    return response





def price(request, price_pattern):
    sorted_price_wise = ""
    price_pattern_heading = ""
    if price_pattern == 'low-high':
        pp = 'price'
        price_pattern_heading = "Price (Lowest ~ Highest)"
        sorted_price_wise  = ProductProfile.objects.all().order_by(pp)
    elif price_pattern == 'high-low':
        pp = '-price'
        price_pattern_heading = "Price (Highest ~ Lowest)"
        sorted_price_wise  = ProductProfile.objects.all().order_by(pp)
    else:
        pass

    context_dict = {'products': sorted_price_wise, 'price_pattern_heading': price_pattern_heading}
    response = render(request,'product/price.html', context_dict)
    return response


def mail_customer_enquriy(form_data_dict):
    name=form_data_dict['name']
    email=form_data_dict['email']
    subject=form_data_dict['subject']
    formatted_subject = "Enquiry @ Dubi Lap: "+subject
    product=form_data_dict['product']
    product_name = product.product_name
    message=form_data_dict['message']
    phone_number=form_data_dict['phone_number']
    formatted_message = "Dear Admin,\n\nYou have recived an Enquiry Regarding "+product_name+" with following particulars:\n\nName: "+name+"\nEmail: "+email+"\nSubject: "+subject+"\nPhone No.: "+phone_number+"\nInterested In: "+product_name+"\n\nMessage:\n\n"+message

    send_mail(formatted_subject,
              formatted_message,
              'enquriy.dubailap@gmail.com',
              ['pleasureinblues@gmail.com'],
              fail_silently=False)


def thank_u_customer(form_data_dict):
    name=form_data_dict['name']
    email=form_data_dict['email']
    subject= "Dubilap | Thank you for Enquiry"
    formatted_message = "Dear "+name+",\n\nThank you for your enquiry.\n\nOne of our representative will contact you soon.\n\nWe hope to have long-term relationship with you.\n\n\nRegards,\n\nDubilap\nwww.dubilap.com"

    send_mail(subject,
              formatted_message,
              'enquriy.dubailap@gmail.com',
              [email],
              fail_silently=False)

def product_inquiry(request, product_id):
    product = ProductProfile.objects.get(pk=product_id)
    if request.method == 'POST':
        #form = Customer_ps_contactForm(request.POST, initial = {'product': product})

        form = Customer_ps_contactForm(initial = {'product': product.id})

        #form = Customer_ps_contactForm(request.POST)

        if form.is_valid():
            form_data_dict = form.cleaned_data
            mail_customer_enquriy(form_data_dict)
            thank_u_customer(form_data_dict)

            form = form.save(commit=False)
            form.product = product
            form.save()
            return home(request)
        else:
            print (form.errors)
    else:
        form = Customer_ps_contactForm()

    context_dict = {'form':form, 'product': product}

    return render(request, 'product/product_inquiry2.html',context_dict)


def handler404(request):
    response = render('404.html', {'context_instace':request})
    response.status_code = 404
    return response