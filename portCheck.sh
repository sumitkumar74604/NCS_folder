#!/bin/bash

# Check if port 8000 is already in use
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "Port 8000 is already in use. Killing the process..."
    # Kill the process using port 8000
    kill $(lsof -t -i:8000)
    echo "Process killed successfully."
else
    echo "Port 8000 is not in use."
fi
