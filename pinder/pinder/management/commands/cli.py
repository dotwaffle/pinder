from django.core.management.base import BaseCommand

from peering_requests.models import Request


class Command(BaseCommand):

    help = "A CLI script.  Whatever you like can be here."

    def handle(self, *args, **options):
        print(args)
        print(options)

        print("Your custom stuff lives here")

