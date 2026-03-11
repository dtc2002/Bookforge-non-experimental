import argparse

def main():
    parser = argparse.ArgumentParser(description='Bookforge CLI')
    parser.add_argument('command', choices=['run', 'test'], help='Command to execute')
    args = parser.parse_args()
    print(f'Executing command: {args.command}')

if __name__ == '__main__':
    main()