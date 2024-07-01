import argparse
from core import create_nginx_config, manage_service


def main():
    parser = argparse.ArgumentParser(description='Python Nginx Configuration Tool')
    parser.add_argument('action', choices=['start', 'stop', 'reload', 'setup'], help='Action to perform')
    parser.add_argument('--server-name', help='Server name for the Nginx configuration')
    parser.add_argument('--app-port', type=int, help='Port of the Python application')

    args = parser.parse_args()

    if args.action == 'setup':
        if not args.server_name or not args.app_port:
            print("server-name and app-port are required for setup")
            return
        create_nginx_config(args.server_name, args.app_port)
    else:
        manage_service(args.action)


if __name__ == '__main__':
    main()
