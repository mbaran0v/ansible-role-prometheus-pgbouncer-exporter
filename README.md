# Ansible role: prometheus-pgbouncer-exporter

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-prometheus-pgbouncer-exporter.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-prometheus-pgbouncer-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-prometheus-pgbouncer-exporter.svg)](https://github.com/mbaran0v/ansible-role-prometheus-pgbouncer-exporter/tags/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for [Prometheus PgBouncer exporter](https://github.com/spreaker/prometheus-pgbouncer-exporter). Currently this works on Debian and RedHat based linux systems (only systemd support). Tested platforms are:

* Ubuntu 16.04
* CentOS 7
* Debian 9

Requirements
------------

Requires Python3; recommended role for Python installation: [geerlingguy.python-pip](https://github.com/geerlingguy/ansible-role-pip.git)

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
pgbouncer_exporter_version: 2.0.1
pgbouncer_exporter_host: 127.0.0.1
pgbouncer_exporter_port: 9127
pgbouncer_exporter_log_level: INFO

# list of environment variables
pgbouncer_exporter_env_variables:
  - PGBOUNCER_PASS=passw0rd!

# pgbouncer supports environment variables replacement
# Ie. $(PGBOUNCER_PASS) is replaced with the content of "PGBOUNCER_PASS" environment variable
pgbouncer_exporter_pgbouncers:
  - dsn: postgresql://pgbouncer:$(PGBOUNCER_PASS)@127.0.0.1:5432/pgbouncer
    connect_timeout: 5
    include_databases: []
    exclude_databases:
      - pgbouncer
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: prometheus-pgbouncer-exporter
  roles:
      - role: mbaran0v.prometheus-pgbouncer-exporter
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2019 by Maxim Baranov.
