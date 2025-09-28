import subprocess
from pathlib import Path
from importlib.resources import files

def build_init_parser(parser):
    subparser = parser.add_parser("build", help="Build provided file.cpp")
    subparser.add_argument("file_name", type=str, help="Name of file to compile")

def build(file_name):
    makefile_path = files('clank.resources').joinpath('Makefile')

    file_path = Path(file_name)
    file_path_extension = Path(file_name + ".cpp").resolve()
    if not file_path_extension.is_file():
        print(f"No file named {file_name}")
        return -1

    cmd = ["make", "-f", makefile_path, file_path]

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("✅ Compilation successful")
    else:
        print("❌ Compilation failed")
    
    return result.returncode
