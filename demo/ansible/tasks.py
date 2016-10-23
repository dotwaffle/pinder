import invoke
import hammock
import json

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pprint import pformat



def pprint_color(obj):
    print highlight(pformat(obj), PythonLexer(), Terminal256Formatter(style='trac'))


@invoke.task
def prepare(ctx):
    invoke.run('ansible-playbook playbook_prepare.yml')


@invoke.task
def deploy_rtr00(ctx):
    invoke.run('ansible-playbook playbook_configure.yml --limit rtr00')


@invoke.task
def deploy_rtr01(ctx):
    invoke.run('ansible-playbook playbook_configure.yml --limit rtr01')


@invoke.task
def verify(ctx):
    invoke.run('ansible-playbook playbook_facts.yml')


@invoke.task
def get_requests(ctx):
    results = invoke.run('../../pinder/manage.py cli --all')


@invoke.task
def complete_requests(ctx):
    pinder = hammock.Hammock('http://127.0.0.1:8000', append_slash=True)
    results = pinder.api.requests.GET().json()['results']

    for r in results:
        r['state'] = 'finished'
        pinder.api.requests(r['id']).PUT(data=r)


@invoke.task
def approve_request(ctx, request_id):
    _requests(request_id, 'in-progress')


def _requests(rid, state, others=None):
    pinder = hammock.Hammock('http://127.0.0.1:8000', append_slash=True)
    current = pinder.api.requests(rid).GET()
    current = current.json()
    current['state'] = state
    result = pinder.api.requests(rid).PUT(data=current).json()
    pprint_color(result)
