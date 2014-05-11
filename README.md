# Ansible Plugins

A collection of new and modified ansible plugins.

## vars_plugins/gpg_vars

Reads group and host variablse in the same style as ansible group_vars and
host_vars, first passing the file through GnuPG in batch mode. Files ending in
.yaml.asc, .yaml.gpg, .yml.asc, and .yml.gpg will be read. Does not support
symetric encryption so you should have an appropriate gpg-agent running.

Modified from the base ansible [group_vars](https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/vars_plugins/group_vars.py)
plugin.
