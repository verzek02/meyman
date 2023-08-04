from rest_framework import serializers

from apps.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id',
                  'news',
                  'hotel',
                  'stars',
                  'comment',
                  'formatted_date_added',
                  )

    def get_average_stars(self, obj):
        reviews = obj.reviews.all()
        total_reviews = reviews.count()
        if total_reviews > 0:
            sum_stars = sum(review.stars for review in reviews)
            return round(sum_stars / total_reviews, 2)
        return 0

    def get_total_reviews(self, obj):
        return obj.reviews.count()
