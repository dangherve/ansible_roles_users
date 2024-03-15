
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def is_user_on_this_srv(user, ansible_fqdn, group_names):
    if "servers_fqdn" in user.keys():
        if ansible_fqdn in user['servers_fqdn']:
            return True
    if "ansible_groups" in user.keys():
        for group in user["ansible_groups"]:
            if group in group_names:
                return True
    return False

def authorized_keys(user):
    if 'authorized_keys' in user.keys():
        return user['authorized_keys']
    else:
        return [user['name'] + '.pub']

class FilterModule(object):

    def filters(self):
        return {
            'is_user_on_this_srv': is_user_on_this_srv,
            'authorized_keys': authorized_keys,
        }

