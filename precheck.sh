#!/bin/bash

set -e

echo "Precheck Script"

/usr/bin/python3.11 /usr/local/bin/validation/precheck.py

echo "Precheck completed successfully"
