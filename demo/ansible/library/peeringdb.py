#!/usr/bin/python
# -*- coding: utf-8 -*-

mocked_data = {
    65100: {
        "id": 25649,
        "net_id": 5520,
        "ix_id": 781,
        "name": "RainbowXP",
        "ixlan_id": 781,
        "notes": "",
        "speed": 10000,
        "asn": 65100,
        "ipaddr4": "10.0.0.0",
        "ipaddr6": None,
        "is_rs_peer": False,
        "created": "2015-11-02T00:00:00Z",
        "updated": "2016-03-16T16:49:58Z",
        "status": "ok"
    },
    65200: {
        "id": 25650,
        "net_id": 5520,
        "ix_id": 781,
        "name": "RainbowXP",
        "ixlan_id": 781,
        "notes": "",
        "speed": 10000,
        "asn": 65200,
        "ipaddr4": "10.0.0.1",
        "ipaddr6": None,
        "is_rs_peer": False,
        "created": "2015-11-02T00:00:00Z",
        "updated": "2016-03-16T16:49:58Z",
        "status": "ok"
    },
}

def main():
    module = AnsibleModule(
        argument_spec=dict(
            accepted_requests=dict(type='list', required=True),
        ),
        supports_check_mode=True
    )
    accepted_requests = module.params['accepted_requests']

    peering_info = mocked_data
    module.exit_json(peering_info=peering_info, msg=str(peering_info))


from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
