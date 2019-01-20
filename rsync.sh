#!/bin/bash
find . -type f -not -path "./core/*" -not -name "*.json" -not -name "rsync.sh" -exec rm {} \;
rsync -avzh --exclude .git --exclude *.swp --exclude *.swo --copy-links
miffi@iroh:~/dev/Voice-Coding /mnt/c/NatLink/NatLink/MacroSystem
find . -type f -name "*.py" -exec touch {} \;
