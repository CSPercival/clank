import subprocess
from pathlib import Path
import os
import sys

def run_init_parser(parser):
    subparser = parser.add_parser("run", help="Run provided exec")
    subparser.add_argument("exe_name", type=str, help="Name of executable file")
    subparser.add_argument("input_file", nargs="?", type=str, help="Name of the input file")
    subparser.add_argument("output_file", nargs="?", type=str, help="Name of the output file")

def run(exe_name, input_file, output_file):
    exe_path = Path(exe_name).resolve()
    if not exe_path.is_file():
        print(f"No executable file named {exe_name}")
        return

    if not input_file:    
        process = subprocess.run(exe_path, stderr=subprocess.PIPE)
    else:
        input_path = Path(input_file).resolve()
        if not input_path.is_file():
            print(f"No input file named {exe_name}")
            return

        if not output_file:
            with input_path.open("r") as fin:
                process = subprocess.run(exe_path, stdin=fin, stderr=subprocess.PIPE, text=True)
        else:
            output_path = Path(output_file).resolve()
            with input_path.open("r") as fin, output_path.open("w") as fout:
                    process = subprocess.run(exe_path, stdin=fin, stdout=fout, stderr=subprocess.PIPE, text=True)
    
    if process.returncode == 0:
        print("✅ Execution completed successfully.", file=sys.stderr)
    else:
        print("❌ Execution failed:", process.returncode, file=sys.stderr)
        print("Message: ", process.stderr, file=sys.stderr)