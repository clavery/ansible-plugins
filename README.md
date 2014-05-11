# Ansible Plugins

A collection of new and modified ansible plugins.

## vars_plugins/gpg_vars

Reads group and host variablse in the same style as ansible group_vars and
host_vars, first passing the file through GnuPG in batch mode. Files ending in
.yaml.asc, .yaml.gpg, .yml.asc, and .yml.gpg will be read. Does not support
symetric encryption so you should have an appropriate gpg-agent running.

Modified from the base ansible [group_vars](https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/vars_plugins/group_vars.py)
plugin.

This is an alternative to the built-in [ansible
vault](http://docs.ansible.com/playbooks_vault.html). Use that feature if you
need simpler, password-based, encryption.

### Usage

Place encrypted yaml files in a `secrets/` folder relative to your inventory
file or playbook. Variables imported 

Example:

```
project_root/
    - inventory.ini
    - deploy.yaml
    - group_vars
        - all.yaml
    - secrets
        - group_vars
            - all.yaml.asc
            - webservers.yaml.asc
        - host_vars
            - gamma.yaml.asc
```
