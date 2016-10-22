#!/usr/bin/python
# -*- coding: utf-8 -*-

mocked_data = [
    (65100, 65200, 781, 'accepted', ''),
]

def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', required=True, choices=['pending', 'accepted', 'rejected']),
        ),
        supports_check_mode=True
    )
    state = module.params['state']

    sessions = mocked_data
    module.exit_json(sessions=sessions, msg=str(sessions))


from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
