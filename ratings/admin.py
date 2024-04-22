from django.contrib import admin
from .models import RatingsAndReviews

class RatingAndReviewAdmin(admin.ModelAdmin):
    list_display=('customer', 'business', 'review', 'rating', 'date_of_review')
admin.site.register(RatingsAndReviews, RatingAndReviewAdmin)
