from setuptools import setup, find_packages

setup(
    name='python_nginx',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jinja2',  # For templating Nginx configuration
        'requests',  # For SSL certificate requests
    ],
    entry_points={
        'console_scripts': [
            'python_nginx=python_nginx.cli:main',
        ],
    },
)
