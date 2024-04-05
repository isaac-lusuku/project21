from django.db import models
from main_info.models import MyUser
from businesses.models import Business

"""
these are the models for handling the ratings and reviews
"""

class RatingsAndReviews(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    review = models.TextField(max_length= 200, blank=True)
    rating = models.IntegerField()
    date_of_review = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return " ".join(self.review.split(" ")[20])
