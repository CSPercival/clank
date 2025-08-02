#!/bin/bash

MAIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLANK="$MAIN_DIR/run_clank.py"

#Permission
echo "Give permission to clank"
chmod +x "$CLANK"

#Symlink
echo "Create symlink"
sudo ln -sf "$CLANK" /usr/local/bin/clank

#Test
if command -v clank &> /dev/null; then
    echo "Installation completed successfully"
else
    echo "Installation crashed!"
fi