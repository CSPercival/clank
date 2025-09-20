# Clank
Clank is a lightweight Python script that automates common competitive programming tasks.

## ✨ Features

### Available Commands

- **Greet**
  ```bash
  clank greet
  ```
  Prints a greeting message.

- **Clean**
  ```bash
  clank clean
  ```
  Removes all binary files generated from matching `.cpp` files.

- **Prepare Codeforces Contest**
  ```bash
  clank cf <number_of_problems> [prefix]
  ```
  Creates `<number_of_problems>` source files named using the given `<prefix>` (if provided) followed by consecutive letters of the alphabet. 
  
  If prefix is omitted, it defaults to an empty string `""`.

  Each file is pre-filled with a `.cpp` template.  

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
  