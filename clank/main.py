
import argparse
from clank.commands.greet import greet
from clank.commands.clean import clean_bin_files
from clank.commands.prepare_files import prepare_files

def main():
    parser = argparse.ArgumentParser(description = "Tool for automating competitive programming related tasks")

    parser.add_argument("--greet", action="store_true", help="Print greeting message")
    parser.add_argument("--cf", nargs = 2, type = str, help="Create files for contest")
    parser.add_argument("--clean", action="store_true", help="clean binary files")

    args = parser.parse_args()

    if args.greet:
        greet()

    if args.clean:
        clean_bin_files()
    
    if args.cf:
        prefix, number_of_problems = args.cf
        prepare_files(prefix, int(number_of_problems))