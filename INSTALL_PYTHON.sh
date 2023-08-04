#!/bin/bash

# Install Homebrew if not already installed
if ! command -v brew >/dev/null; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi

# Update Homebrew
brew update

# Install latest Python 3
brew install python

# Set new Python3 as default Python
brew link python --force

# Check new default Python version
python --version
