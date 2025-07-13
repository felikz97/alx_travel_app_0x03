from django.core.management.base import BaseCommand
from listings.models import Listing
from listings.serializers import ListingSerializer
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        Listing.objects.all().delete()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                location=fake.city(),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.randint(30, 500),
                available=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded sample listings."))
