import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['hello'])
    args = parser.parse_args()

    if args.command == 'hello':
        print("Welcome to bookforge!")

if __name__ == '__main__':
    main()