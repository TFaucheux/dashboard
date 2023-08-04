#!/bin/bash
set -xv

# remove old directory
# (careful as this will destroy any changes)
rm -rf dashboard 2>/dev/null

# Create virtual environment
python3 -m venv dashboard

# Activate environment
source dashboard/bin/activate

# upgrade version of pip
pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --upgrade pip

# Install requirements
pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

# Install watchdog to made rendering of changes faster
pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org watchdog

# Copy app code
cp dashboard.py dashboard/

cd dashboard
# create logo.png file if missing, before executing (must be a valid image file).
wget -O logo.png https://brandslogos.com/wp-content/uploads/images/large/acme-logo.png
ls -l logo.png
