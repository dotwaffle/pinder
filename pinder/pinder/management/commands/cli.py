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
        parser.add_argument('--update', type=int,
            help='Set state to finish for specified id')
        parser.add_argument('--update-all', action='store_true',
            default='False', help='Set state to finish for all entries in db')


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

    def update_state(self, data):
        url = "http://localhost:8000/api/requests/{}/".format(data['id'])
        headers = {'content-type': 'application/json'}
        data['state'] = 'finished'
        resp = requests.put(url, json=data, headers=headers)
        if resp.status_code != 200:
            raise CommandError('PUT /requests/ {}'.format(data['id']))
        else:
            print("id {} status successfully set to finished".format(data['id']))

    def get_entry(self, rid):
        url = "http://localhost:8000/api/requests/{}".format(rid)
        req = requests.get(url)
        if req.status_code != 200:
            raise CommandError('GET /requests/ {}'.format(req.status_code))
        else:
            return req.json()

    def get_all(self):
        url = "http://localhost:8000/api/requests/"
        reqs = requests.get(url)
        if reqs.status_code != 200:
            raise CommandError('GET /requests/ {}'.format(reqs.status_code))
        else:
            return reqs.json()['results']

    def handle(self, *args, **options):
        if options['state']:
            for entry in options['state']:
                entry_data = self.get_entry(entry)
                print(self.display_entry_data(entry_data))
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
        elif options['update']:
            entry_data = self.get_entry(options['update'])
            self.update_state(entry_data)
        elif options['update_all'] is True:
            reqs = self.get_all()
            for req in reqs:
                self.update_state(req)
        else:
            reqs = requests.get('http://localhost:8000/api/requests/')
            if reqs.status_code != 200:
                raise CommandError('GET /requests/ {}'.format(reqs.status_code))
            else:
                result = reqs.json()
                for req in result['results']:
                    print(self.display_entry_data(req))
