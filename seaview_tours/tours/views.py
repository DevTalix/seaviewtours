from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    Service,
    TourPackage,
    ContactMessage,
    Booking,
    Testimonial
)


# ---------------- HOME ----------------
def home(request):
    featured_tours = TourPackage.objects.filter(
        is_featured=True,
        is_active=True
    )[:3]

    testimonials = Testimonial.objects.filter(
        is_approved=True
    )[:3]

    return render(request, 'tours/index.html', {
        'featured_tours': featured_tours,
        'testimonials': testimonials,
        'page_title': "SeaView Tours & Travel - Uganda's Premier Travel Company"
    })


# ---------------- ABOUT ----------------
def about(request):
    return render(request, 'tours/about.html', {
        'page_title': 'About Us | SeaView Tours & Travel'
    })


# ---------------- SERVICES ----------------
def services(request):
    services_list = Service.objects.filter(is_active=True)

    return render(request, 'tours/services.html', {
        'services': services_list,
        'page_title': 'Our Services | SeaView Tours & Travel'
    })


# ---------------- SERVICE DETAIL ----------------
def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)

    return render(request, 'tours/service_detail.html', {
        'service': service,
        'page_title': f'{service.get_name_display()} | SeaView Tours'
    })


# ---------------- CONTACT ----------------
def contact(request):
    """Contact page view"""
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Save to database (if you have ContactMessage model)
        try:
            from .models import ContactMessage
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                service_needed=service,
                message=message
            )
            return JsonResponse({'success': True, 'message': 'Thank you! Your message has been sent.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Error saving message.'})
    
    # Regular GET request
    context = {
        'page_title': 'Contact Us | SeaView Tours & Travel',
    }
    return render(request, 'tours/contact.html', context)

# ---------------- BOOKING ----------------
def booking(request):
    """Booking page view with tour preselection"""

    # Handle tour from URL (?tour=ID)
    tour_id = request.GET.get('tour')
    selected_tour = None

    if tour_id:
        try:
            selected_tour = TourPackage.objects.get(
                id=int(tour_id),
                is_active=True
            )
        except (TourPackage.DoesNotExist, ValueError):
            selected_tour = None

    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        phone = request.POST.get('phone')
        booking_details = request.POST.get('bookingDetails', '')
        tour_id = request.POST.get('tour_id')

        booking = Booking.objects.create(
            customer_name=full_name,
            customer_phone=phone,
            booking_details=booking_details,
        )

        if tour_id:
            try:
                booking.tour = TourPackage.objects.get(id=tour_id)
                booking.save()
            except TourPackage.DoesNotExist:
                pass

        return JsonResponse({
            'success': True,
            'whatsapp_message': (
                f"Hello SeaView Tours! I'd like to book "
                f"{booking.tour.title if booking.tour else 'a trip'}. "
                f"Name: {full_name}, Phone: {phone}. "
                f"Details: {booking_details}"
            )
        })

    services_list = Service.objects.filter(is_active=True)

    return render(request, 'tours/booking.html', {
        'services': services_list,
        'selected_tour': selected_tour,
        'page_title': 'Book Your Trip | SeaView Tours & Travel',
    })


# ---------------- TOURS LIST ----------------
def tours(request):
    tours_list = TourPackage.objects.filter(is_active=True)

    return render(request, 'tours/tours.html', {
        'tours': tours_list,
        'page_title': 'Tour Packages | SeaView Tours & Travel'
    })


# ---------------- TOUR DETAIL ----------------
def tour_detail(request, tour_id):
    tour = TourPackage.objects.get(id=tour_id)

    return render(request, 'tours/tour_detail.html', {
        'tour': tour,
        'page_title': f'{tour.title} | SeaView Tours'
    })


# ---------------- TRAVEL TIPS ----------------
# tours/views.py - travel_tips function
def travel_tips(request):
    """Travel Tips page"""
    context = {
        'page_title': 'Travel Tips | SeaView Tours & Travel',
    }
    return render(request, 'tours/travel_tips.html', context)
