#!/usr/bin/python
# -*- coding: utf-8 -*-

import hammock


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', required=True, choices=['in-progress']),
        ),
        supports_check_mode=True
    )
    state = module.params['state']

    pinder = hammock.Hammock('http://127.0.0.1:8000')

    sessions = pinder.api.requests.GET(params='state={}'.format(state)).json()['results']
    module.exit_json(sessions=sessions, msg=str(sessions))


from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
