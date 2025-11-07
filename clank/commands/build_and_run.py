from clank.commands.build import build
from clank.commands.run import run

def build_and_run_init_parser(parser):
    subparser = parser.add_parser("bar", help="Build and run provided .cpp file")
    subparser.add_argument("file_name", type=str, help="Name of file to compile and run")
    subparser.add_argument("input_file", nargs="?", type=str, help="Name of the input file")
    subparser.add_argument("output_file", nargs="?", type=str, help="Name of the output file")
    subparser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

def build_and_run(file_name, input_file, output_file, debug_option_enabled):
    if build(file_name, debug_option_enabled) == 0:
        run(file_name, input_file, output_file)
    