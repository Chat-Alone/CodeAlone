#!/bin/bash
set -euo pipefail

VENV_NAME="venv"
PYTHON_CMD="python3"
REQUIREMENTS_FILE="requirements.txt"
APP_FILE="app.py"

cd "$(dirname "${BASH_SOURCE[0]}")"

echo "--- Checking for Python 3..."
if ! command -v $PYTHON_CMD &> /dev/null
then
    echo "Error: python3 is not installed or not in PATH."
    exit 1
fi

echo "--- Setting up virtual environment in ./${VENV_NAME}"
if [ ! -d "$VENV_NAME" ]; then
    $PYTHON_CMD -m venv $VENV_NAME
    echo "Virtual environment created."
fi

echo "--- Activating virtual environment..."
source "${VENV_NAME}/bin/activate"

echo "--- Checking for requirements file..."
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "Error: ${REQUIREMENTS_FILE} not found."
    deactivate
    exit 1
fi

echo "--- Installing/updating dependencies..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

echo "--- Checking for application file..."
if [ ! -f "$APP_FILE" ]; then
    echo "Error: ${APP_FILE} not found."
    deactivate
    exit 1
fi

echo ""
echo "============================================="
echo "  Setup complete. Starting the server..."
echo "  URL: http://0.0.0.0:16666"
echo "  Press Ctrl+C to stop the server."
echo "============================================="
echo ""

$PYTHON_CMD $APP_FILE