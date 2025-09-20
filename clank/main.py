
import argparse
from clank.commands.greet import greet
from clank.commands.greet import greet_init_parser
from clank.commands.clean import clean_bin_files
from clank.commands.clean import clean_bin_files_init_parser
from clank.commands.prepare_files import prepare_files
from clank.commands.prepare_files import prepare_files_init_parser
from clank.commands.run import run
from clank.commands.run import run_init_parser

def main():
    parser = argparse.ArgumentParser(description = "Tool for automating competitive programming related tasks")

    subparsers = parser.add_subparsers(dest="command")

    greet_init_parser(subparsers)
    clean_bin_files_init_parser(subparsers)
    prepare_files_init_parser(subparsers)
    run_init_parser(subparsers)

    args = parser.parse_args()

    if args.command == "greet":
        greet()
    elif args.command == "clean":
        clean_bin_files()
    elif args.command == "cf":
        prepare_files(int(args.number_of_problems), args.prefix)
    elif args.command == "run":
        run(args.exe_name, args.input_file, args.output_file)
        