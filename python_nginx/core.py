import os
from jinja2 import Template

NGINX_TEMPLATE = """
server {
    listen 80;
    server_name {{ server_name }};

    location / {
        proxy_pass http://127.0.0.1:{{ app_port }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
"""


def create_nginx_config(server_name, app_port, output_path='nginx.conf', symlink_path=None):
    template = Template(NGINX_TEMPLATE)
    config = template.render(server_name=server_name, app_port=app_port)

    with open(output_path, 'w') as f:
        f.write(config)

    if symlink_path:
        os.symlink(output_path, symlink_path)


def manage_service(action):
    os.system(f'systemctl {action} nginx')
