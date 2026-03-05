# Literary AI CLI
import sys

def main():
    print("Welcome to Literary AI GUI")
    while True:
        cmd = input("Enter command (add, edit, list, exit): ").strip()
        if cmd == 'exit':
            break
        elif cmd == 'add':
            print("Adding new scene...")
        elif cmd == 'edit':
            print("Editing scene...")
        elif cmd == 'list':
            print("Listing scenes...")
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()