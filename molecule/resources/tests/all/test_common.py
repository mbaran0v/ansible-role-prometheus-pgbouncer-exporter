
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_conf_dir(host):
    f = host.file('/etc/pgbouncer_exporter')

    assert f.exists
    assert f.is_directory


def test_log_dir(host):
    f = host.file('/var/log/pgbouncer_exporter')

    assert f.exists
    assert f.is_directory


def test_service(host):
    s = host.service('pgbouncer_exporter')

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user('postgres')

    assert u.exists


def test_group(host):
    g = host.group('postgres')

    assert g.exists


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9127")

    assert s.is_listening


def test_version(host):
    g = pip_package.get_packages()
    for k, v in g.items():
        if k == "prometheus-pgbouncer-exporter":
            version = v['version']
            break

    assert version == "2.0.1"
