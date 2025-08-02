import argparse

def greet():
    print("Hello, my name is Clank.")
    print("What can I do for you?")

def prepare_files(prefix, number_of_problems):
    print("Preparing files")
    for i in range(number_of_problems):
        path = prefix + chr(i + ord('A')) + ".txt"

        with open(path, 'w') as file:
            file.write("Clank was here")
            
        print(f"Created {path} file")

def main():
    parser = argparse.ArgumentParser(description = "Tool for automating competitive programming related tasks")

    parser.add_argument("--greet", action="store_true", help="Print greeting message")
    parser.add_argument("--cf", nargs = 2, type = str, help="Create files for contest")

    args = parser.parse_args()

    if args.greet:
        greet()
    
    if args.cf:
        prefix, number_of_problems = args.cf
        prepare_files(prefix, int(number_of_problems))