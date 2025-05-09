from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import *
import json
from django.contrib import messages
import re

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def united_kingdom(request):
    return render(request, 'united_kingdom.html')

def australia(request):
    return render(request, 'australia.html')

def canada(request):
    return render(request, 'canada.html')

def usa(request):
    return render(request, 'usa.html')

def france(request):
    return render(request, 'france.html')

def malta(request):
    return render(request, 'malta.html')

def denmark(request):
    return render(request, 'denmark.html')

def south_korea(request):
    return render(request, 'south_korea.html')

def hungary(request):
    return render(request, 'hungary.html')

def germany(request):
    return render(request, 'germany.html')

def blogs(request):
    return render(request, 'blogs.html')

def faqs(request):
    return render(request, 'faqs.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')

def location(request):
    return render(request, 'location.html')



@require_POST
def submit_contact(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate all fields are present
        if not all([name, email, message]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
        
        # Name validation (letters, spaces, hyphens, apostrophes, 2-50 chars)
        if not re.match(r'^[a-zA-Z\s\-\']{2,50}$', name):
            return JsonResponse({'status': 'error', 'message': 'Please enter a valid name.'}, status=400)
        
        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return JsonResponse({'status': 'error', 'message': 'Please enter a valid email address.'}, status=400)
        
        # Message validation (basic sanitization, 10-2000 chars)
        if len(message) < 10 or len(message) > 2000:
            return JsonResponse({'status': 'error', 'message': 'Message must be between 10 and 2000 characters.'}, status=400)
        
        # Check for potential HTML/script tags
        if re.search(r'<[^>]*script[^>]*>', message, re.IGNORECASE):
            return JsonResponse({'status': 'error', 'message': 'Invalid characters in message.'}, status=400)
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        return JsonResponse({'status': 'success', 'message': 'Thank you for your message! We will get back to you soon.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)



@require_POST
def book_consultation(request):
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

    try:
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        form = ConsultationForm(data)
        
        # Validate phone number if present
        if 'phone' in data and data['phone']:
            if not re.match(r'^\+?[\d\s\-\(\)]{7,20}$', data['phone']):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please enter a valid phone number.'
                }, status=400)
        
        # Validate name if present
        if 'name' in data and data['name']:
            if not re.match(r'^[a-zA-Z\s\-\']{2,50}$', data['name']):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please enter a valid name.'
                }, status=400)
        
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your request! We\'ll get back to you soon.'
            })
        else:
            errors = form.errors.as_json()
            return JsonResponse({
                'status': 'error',
                'message': 'Please correct the errors below: ' + errors
            }, status=400)
            
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }, status=500)




def become_a_partner(request):
    if request.method == 'POST':
        form = PartnerApplicationForm(request.POST)
        
        # Validate company name
        if 'company_name' in request.POST:
            company_name = request.POST['company_name'].strip()
            if not re.match(r'^[a-zA-Z0-9\s\-\.,&]{2,100}$', company_name):
                messages.error(request, 'Please enter a valid company name.')
                return redirect('become_a_partner')
        
        # Validate website URL if provided
        if 'website' in request.POST and request.POST['website']:
            website = request.POST['website'].strip()
            if not re.match(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', website):
                messages.error(request, 'Please enter a valid website URL.')
                return redirect('become_a_partner')
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your application! We will contact you soon.')
            return redirect('become_a_partner')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PartnerApplicationForm()
    
    return render(request, 'become_a_partner.html', {'form': form})