from django.core.management.base import BaseCommand, CommandError

import requests

class DataWrapper:
    def __init__(self, dict_data=None):
        self._data = dict_data or {}

    @classmethod
    def _wrap_type(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls._wrap_type(d) for d in data]
        else:
            return data

    def __getattr__(self, name):
        try:
            attr = self._data[name]
        except KeyError:
            raise AttributeError(name)
        return self._wrap_type(attr)

class Command(BaseCommand):

    help = "A CLI script.  Whatever you like can be here."

    def add_arguments(self, parser):
        parser.add_argument('--state', nargs='+', type=int,
            help='Get info for specified id')
        parser.add_argument('--all', action='store_true', default='True',
            help='List all entries in db')
        parser.add_argument('--filter', type=str,
            help='Display entries based upon specified state.')


    def display_entry_data(self, data):
        req_data = DataWrapper(data)
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
            req_data.id,
            req_data.sender.name,
            req_data.receiver.name,
            req_data.state,
            req_data.sender_is_ready,
            req_data.receiver_is_ready,
            req_data.created,
            req_data.modified,
            )

    def filter_state(self, state, data):
        return_lst = []
        for entry in data['results']:
            if entry['state'] == state:
                return_lst.append(entry)
        return return_lst

    def handle(self, *args, **options):
        if options['state']:
            for entry in options['state']:
                url = "http://localhost:8000/api/requests/{}".format(entry)
                req = requests.get(url)
                if req.status_code != 200:
                    raise CommandError('GET /requests/ {}'.format(req.status_code))
                else:
                    result = req.json()
                    print(self.display_entry_data(result))
        elif options['filter']:
            reqs = requests.get('http://localhost:8000/api/requests/')
            if reqs.status_code != 200:
                raise CommandError('GET /requests/ {}'.format(reqs.status_code))
            else:
                result = reqs.json()
                filtered = self.filter_state(options['filter'], result)
                print("Found {} entries matching state {}".format(
                    len(filtered), options['filter']))
                for entry in filtered:
                    print(self.display_entry_data(entry))
        else:
            reqs = requests.get('http://localhost:8000/api/requests/')
            if reqs.status_code != 200:
                raise CommandError('GET /requests/ {}'.format(reqs.status_code))
            else:
                result = reqs.json()
                for req in result['results']:
                    print(self.display_entry_data(req))
