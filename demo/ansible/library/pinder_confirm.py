#!/usr/bin/python
# -*- coding: utf-8 -*-

import hammock


def main():
    module = AnsibleModule(
        argument_spec=dict(
            sessions=dict(type='list', required=True),
            asn=dict(type='int', required=True),
        ),
        supports_check_mode=True
    )
    sessions = module.params['sessions']
    asn = module.params['asn']

    pinder = hammock.Hammock('http://127.0.0.1:8000', append_slash=True)
    result = []
    for session in sessions:
        if session['sender']['isp']['asn'] == asn:
            session['sender_is_ready'] = True
        elif session['receiver']['asn'] == asn:
            session['receiver_is_ready'] = True
        else:
            raise Exception("Couldn't figure out if I was the sender or the receiver")
        r = pinder.api.requests(session['id']).PUT(data=session)
        result.append(r.json())
    module.exit_json(sessions=result, msg=str(result))


from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
