import argparse

def greet():
    print("Hello, my name is Clank.")
    print("What can I do for you?")

def main():
    parser = argparse.ArgumentParser(description = "Tool for automating competitive programming related tasks")

    parser.add_argument("--greet", action="store_true", help="Print greeting message")

    args = parser.parse_args()

    if args.greet:
        greet()