import invoke


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
