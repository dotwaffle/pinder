from django.core.management.base import BaseCommand

import requests

class Command(BaseCommand):

    help = "A CLI script.  Whatever you like can be here."

    def add_arguments(self, parser):
        parser.add_argument('--state', nargs='+', type=int)
        parser.add_argument('--all', action='store_true', default='True',
            help='List all entries in db')

    def display_entry_data(self, entry):
        template = """
            id: {}
            sender: {}
            receiver: {}
            state: {}
            sender_is_ready: {}
            receiver_is_ready: {}
            created: {}
            modified: {}
        """
        return template.format(
            entry['id'],
            entry['sender']['name'],
            entry['receiver']['name'],
            entry['state'],
            entry['sender_is_ready'],
            entry['receiver_is_ready'],
            entry['created'],
            entry['modified'],
            )

    def get_entry(self, entry):
        pass

    def handle(self, *args, **options):
        if options['state']:
            for entry in options['state']:
                url = "http://localhost:8000/api/requests/{}".format(entry)
                req = requests.get(url)
                if req.status_code != 200:
                    raise ApiError('GET /requests/ {}'.format(reqs.status_code))
                else:
                    result = req.json()
                    print(self.display_entry_data(result))
        else:
            reqs = requests.get('http://localhost:8000/api/requests/')
            if reqs.status_code != 200:
                raise ApiError('GET /requests/ {}'.format(reqs.status_code))
            else:
                result = reqs.json()
                for req in result['results']:
                    print(self.display_entry_data(req))
