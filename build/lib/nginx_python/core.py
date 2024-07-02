import os
from jinja2 import Template
from .template import NGINX_TEMPLATE


def create_nginx_config(
        server_name,
        app_port,
        app_name,
        use_ssl=False,
        ssl_certificate_path=None,
        ssl_certificate_key_path=None,
        output_path='nginx_conf',
        symlink_path=None):
    template = Template(NGINX_TEMPLATE)
    config = template.render(
        server_name=server_name,
        app_port=app_port,
        use_ssl=use_ssl,
        app_name=app_name,
        ssl_certificate_path=ssl_certificate_path,
        ssl_certificate_key_path=ssl_certificate_key_path
    )

    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Write the configuration file
    config_file_path = os.path.join(output_path, 'nginx.conf')
    with open(config_file_path, 'w') as f:
        f.write(config)

    # Create a symbolic link if specified
    if symlink_path:
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
        os.symlink(config_file_path, symlink_path)


def manage_service(action):
    os.system(f'systemctl {action} nginx')
