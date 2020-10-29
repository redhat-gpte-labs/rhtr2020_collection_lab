#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: my_module
version_added: historical
short_description: TOutput a string
description:
   - A trivial test module, this looks like it was based on ping
   - ssh or local connections only
options:
  data:
    description:
      - Data to return for the C(ping) return value.
      - If this parameter is set to C(crash), the module will cause an exception.
    type: str
    default: Hello RHTR!  This is my new module, borrowed from somewhere!
author:
    - Unknown
    - Michael DeHaan?
'''

EXAMPLES = '''
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m my_module
- name: Example from an Ansible Playbook
  my_module:
- name: Induce an exception to see what happens
  my_module:
    data: crash
'''

RETURN = '''
my_module:
    description: value provided with the data parameter
    returned: success
    type: str
    sample: Hello RHTR!  This is my new module, borrowed from somewhere!
'''

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
