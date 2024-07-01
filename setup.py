from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    long_description=long_description,
    long_description_content_type="text/markdown",  # Use "text/x-rst" if you have README.rst
)
