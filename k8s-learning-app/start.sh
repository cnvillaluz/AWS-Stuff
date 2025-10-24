#!/bin/bash
# Kubernetes Learning App - Quick Start Script

echo "=========================================="
echo "Kubernetes Learning Application"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "Python 3 found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing required dependencies..."
    pip3 install -r requirements.txt
else
    echo "Dependencies already installed."
fi

echo ""
echo "Starting Kubernetes Learning Application..."
echo "=========================================="
echo ""
echo "The application will be available at:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Change to web-app directory and run
cd web-app
python3 app.py
