#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='Hello RHTR!  This is my new module, borrowed from somewhere!'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        my_new_module_result=module.params['data'],
    )
    module.exit_json(**result)


if __name__ == '__main__':
    main()
