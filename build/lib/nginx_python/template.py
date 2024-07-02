NGINX_TEMPLATE = """
server {
    listen 80;
    server_name {{ server_name }};

    location / {
        proxy_pass http://{{ app_name }}:{{ app_port }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    {% if use_ssl %}
    listen 443 ssl;
    server_name {{ server_name }};

    ssl_certificate /etc/nginx/certs/{{ ssl_certificate_path }};
    ssl_certificate_key /etc/nginx/certs/{{ ssl_certificate_key_path }};

    location / {
        proxy_pass http://{{ app_name }}:{{ app_port }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Referer $http_referer;
    }
    location /static/ {
        alias /app/{{ app_name }}/static/;
    }
    {% endif %}
}
"""
