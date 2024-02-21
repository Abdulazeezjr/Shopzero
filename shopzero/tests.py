from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Product, Review

class ReviewTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            price=10.0,
            quantity=100,
            description='Test description',
            release_date='2024-02-10'
        )

    def test_create_review(self):
        # Create a review
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=5,
            comment='Great product!'
        )

        # Retrieve the review from the database
        saved_review = Review.objects.get(pk=review.pk)

        # Check if the retrieved review matches the created review
        self.assertEqual(saved_review.user, self.user)
        self.assertEqual(saved_review.product, self.product)
        self.assertEqual(saved_review.rating, 5)
        self.assertEqual(saved_review.comment, 'Great product!')

    def test_get_reviews_for_product(self):
        # Create multiple reviews for the same product
        Review.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment='Good product!'
        )
        Review.objects.create(
            user=self.user,
            product=self.product,
            rating=3,
            comment='Average product'
        )

        # Retrieve all reviews for the product
        reviews = Review.objects.filter(product=self.product)

        # Check if the correct number of reviews is retrieved
        self.assertEqual(reviews.count(), 2)
