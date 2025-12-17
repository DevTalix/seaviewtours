# tours/admin.py
from django.contrib import admin
from .models import Service, TourPackage, Testimonial, Booking, ContactMessage, GalleryImage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'processing_time', 'is_active')
    list_filter = ('is_active', 'name')
    search_fields = ('description', 'requirements')

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'package_type', 'price', 'duration_days', 'is_featured', 'is_active')
    list_filter = ('package_type', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'overview')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved')
    search_fields = ('client_name', 'content')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'booking_type', 'status', 'created_at')
    list_filter = ('status', 'whatsapp_sent', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_needed', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'description')