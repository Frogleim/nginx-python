import unittest
import os
from python_nginx.core import create_nginx_config, manage_service

class TestPythonNginx(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_nginx_config'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_create_nginx_config(self):
        server_name = 'example.com'
        app_port = 8000
        output_path = os.path.join(self.test_dir, 'nginx.conf')
        symlink_path = os.path.join(self.test_dir, 'default')

        create_nginx_config(server_name, app_port, output_path, symlink_path)

        with open(output_path, 'r') as f:
            config = f.read()

        self.assertIn('server_name example.com', config)
        self.assertIn('proxy_pass http://127.0.0.1:8000', config)
        self.assertTrue(os.path.islink(symlink_path))
        self.assertEqual(os.readlink(symlink_path), output_path)

    def test_manage_service(self):
        # Mock the os.system call to prevent actual service management
        import os
        from unittest.mock import patch

        with patch('os.system') as mocked_system:
            manage_service('start')
            mocked_system.assert_called_with('systemctl start nginx')

if __name__ == '__main__':
    unittest.main()
