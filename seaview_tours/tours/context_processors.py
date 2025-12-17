# tours/context_processors.py
from django.db.models import Q

def services_processor(request):
    """Safe context processor - won't crash if models don't exist yet"""
    try:
        from .models import Service, TourPackage, Testimonial
        return {
            'all_services': Service.objects.filter(is_active=True) if Service.objects.exists() else [],
            'featured_tours': TourPackage.objects.filter(is_featured=True, is_active=True)[:3] if TourPackage.objects.exists() else [],
            'testimonials': Testimonial.objects.filter(is_approved=True)[:5] if Testimonial.objects.exists() else [],
            'company_email': 'seaviewreservations2@gmail.com',
            'company_phone': '+256 701 157 839',
            'company_address': 'Zainabu, Aziza Building, Entebbe Road, Level 7:RmC1-6',
        }
    except Exception as e:
        # Return safe defaults if there's any error
        print(f"Context processor error: {e}")
        return {
            'all_services': [],
            'featured_tours': [],
            'testimonials': [],
            'company_email': 'seaviewreservations2@gmail.com',
            'company_phone': '+256 701 157 839',
            'company_address': 'Zainabu, Aziza Building, Entebbe Road, Level 7:RmC1-6',
        }