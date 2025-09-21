# Clank
Clank is a lightweight Python script that automates common competitive programming tasks.

## ✨ Features

### Available Commands

- **Build and Run**
  ```bash
  clank bar <file_name> [input_file] [output_file]
  ```
  Does exactly what you think. Executes **Build** command and after succesfull compilation executes **Run** command.

- **Build**
  ```bash
  clank build <file_name>
  ```
  Execute `make` on `<file_name>` using **Makefile** stored in the **clank/resource** directory.

- **Clean**
  ```bash
  clank clean
  ```
  Removes all binary files generated from matching `.cpp` files.

- **Greet**
  ```bash
  clank greet
  ```
  Prints a greeting message.

- **Prepare Codeforces Contest**
  ```bash
  clank cf <number_of_problems> [prefix]
  ```
  Creates `<number_of_problems>` source files named using the given `<prefix>` (if provided) followed by consecutive letters of the alphabet. 
  
  If prefix is omitted, it defaults to an empty string `""`.

  Each file is pre-filled with a `.cpp` template. 

- **Run**
  ```bash
  clank run <name_file> [input_file] [output_file]
  ```
  Execute `<name_file>` and uses `[input_file]` as an input to the executable file and `[output_file]` to store the output of the execution.
  
  If you want to provide `[output_file]` without providing `[input_file]` try: `clank run <name_file> > <output_file>`

---

## ⚙️ Installation

Clone this repository and run:

```bash
./install.sh
```

After a successful installation, the message
**`Installation completed successfully`**
will appear in the terminal.

---

## 💥 Troubleshooting

- **Issue:** `./install.sh: Permission denied`
- **Solution:** Make the install script executable by running:
  ```bash
  chmod +x install.sh
  ```
  