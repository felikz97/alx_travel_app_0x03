from django.contrib import admin
from .models import Listing, Booking, Review

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'available')
    search_fields = ('title', 'location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'check_in_date', 'check_out_date', 'user')
    list_filter = ('check_in_date', 'check_out_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('listing', 'rating', 'user', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user', 'comment')
