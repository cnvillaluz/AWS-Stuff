#!/bin/bash
# Setup script for Python Learning App

echo "======================================"
echo "Python Learning App - Setup"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.6 or higher from https://www.python.org/"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python version: $PYTHON_VERSION"

# Make main.py executable
chmod +x main.py

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To start learning Python, run:"
echo "  python3 main.py"
echo ""
echo "or simply:"
echo "  ./main.py"
echo ""
echo "Happy learning!"
