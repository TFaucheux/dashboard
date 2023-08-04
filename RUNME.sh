#!/bin/bash
set -xv

# Activate virtual environment
source dashboard/bin/activate

# Run Streamlit app
streamlit run dashboard.py

exit 0
