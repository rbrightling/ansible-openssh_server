""" OpenSSH Server Ansible Jinja Filters """
__metaclass__ = type


def argument_filter(value, join=","):
    """Format a filter from ansible to sshd_config types"""

    if value is True:
        argument = "yes"
    elif value is False:
        argument = "no"
    elif type(value) is list:
        argument = join.join(filter(None, value))
    else:
        argument = value

    return argument


def match_filter(name, value):
    """Format a openssh match option"""
    if type(value) is list:
        match = ",".join(value)
    else:
        match = value

    return "{} {}".format(name, match)


def user_match_filter(value):
    return match_filter("User", value)


def group_match_filter(value):
    return match_filter("Group", value)


def host_match_filter(value):
    return match_filter("Host", value)


def local_address_match_filter(value):
    return match_filter("LocalAddress", value)


def local_port_match_filter(value):
    return match_filter("LocalPort", value)


def address_match_filter(value):
    return match_filter("Address", value)


class FilterModule(object):

    def filters(self):

        return {
            'openssh_server_argument': argument_filter,
            'openssh_server_user_match': user_match_filter,
            'openssh_server_group_match': group_match_filter,
            'openssh_server_host_match': host_match_filter,
            'openssh_server_address_match': address_match_filter,
            'openssh_server_local_address_match': local_address_match_filter,
            'openssh_server_local_port_match': local_port_match_filter
        }
