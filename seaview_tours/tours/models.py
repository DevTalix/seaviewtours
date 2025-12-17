
# tours/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Service(models.Model):
    """Model for all services offered (passport, visa, car hire, etc.)"""
    SERVICE_TYPES = [
        ('passport', 'Passport Processing'),
        ('visa', 'Visa Processing'),
        ('air_ticket', 'Air Ticketing'),
        ('car_hire', 'Car Hire'),
        ('honeymoon', 'Honeymoon Packages'),
        ('interpol', 'Interpol Services'),
        ('national_id', 'National IDs'),
        ('tour', 'Tour Packages'),
    ]
    
    name = models.CharField(max_length=100, choices=SERVICE_TYPES)
    description = models.TextField()
    requirements = models.TextField(help_text="List requirements separated by commas")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    processing_time = models.CharField(max_length=50, help_text="e.g., 3-5 working days")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.get_name_display()
    
    def requirements_list(self):
        return [req.strip() for req in self.requirements.split(',')]

class TourPackage(models.Model):
    """Model for tour packages (safaris, honeymoon, etc.)"""
    PACKAGE_TYPES = [
        ('safari', 'Safari Adventure'),
        ('honeymoon', 'Honeymoon Package'),
        ('beach', 'Beach Trip'),
        ('cultural', 'Cultural Excursion'),
        ('custom', 'Custom Itinerary'),
    ]
    
    title = models.CharField(max_length=200)
    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPES)
    description = models.TextField()
    overview = models.TextField(help_text="Brief overview for listings")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    max_people = models.PositiveIntegerField()
    itinerary = models.TextField(help_text="Day-by-day itinerary")
    includes = models.TextField(help_text="What's included, separated by commas")
    excludes = models.TextField(help_text="What's not included, separated by commas")
    image_url = models.URLField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def includes_list(self):
        return [item.strip() for item in self.includes.split(',')]
    
    def excludes_list(self):
        return [item.strip() for item in self.excludes.split(',')]

class Testimonial(models.Model):
    """Customer testimonials/reviews"""
    client_name = models.CharField(max_length=100)
    client_location = models.CharField(max_length=100, blank=True)
    client_avatar_url = models.URLField(max_length=500, blank=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"

class Booking(models.Model):
    """Model for customer bookings"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, null=True, blank=True)
    booking_details = models.TextField(blank=True, help_text="Additional requirements/notes")
    number_of_travelers = models.PositiveIntegerField(default=1)
    travel_dates = models.CharField(max_length=100, blank=True, help_text="Preferred travel dates")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    whatsapp_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name}"
    
    def booking_type(self):
        if self.service:
            return f"Service: {self.service.get_name_display()}"
        elif self.tour_package:
            return f"Tour: {self.tour_package.title}"
        return "Custom Booking"

class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_needed = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"

class GalleryImage(models.Model):
    """Model for travel gallery images"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500)
    location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title