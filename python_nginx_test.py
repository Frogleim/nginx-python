import os
import pytest
from nginx_python.core import create_nginx_config, manage_service
from unittest.mock import patch


@pytest.fixture(scope='function')
def test_dir():
    dir_path = 'test_nginx_config'
    os.makedirs(dir_path, exist_ok=True)
    yield dir_path
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(dir_path)


def test_create_nginx_config(test_dir):
    server_name = 'example.com'
    app_port = 8000
    output_path = os.path.join(test_dir, 'nginx.conf')
    symlink_path = os.path.join(test_dir, 'default')
    app_name = 'django'
    create_nginx_config(server_name=server_name, app_port=app_port, app_name=app_name, use_ssl=False, output_path=test_dir, symlink_path=symlink_path)

    with open(output_path, 'r') as f:
        config = f.read()

    assert f'server_name {server_name}' in config
    assert f'proxy_pass http://{app_name}:{app_port}' in config
    assert os.path.islink(symlink_path)
    assert os.readlink(symlink_path) == output_path


def test_manage_service():
    with patch('os.system') as mocked_system:
        manage_service('start')
        mocked_system.assert_called_with('systemctl start nginx')


if __name__ == '__main__':
    pytest.main()
