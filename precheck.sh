#!/bin/bash

set -e

echo "Precheck Script"

ls -l /runner/env >&2 || echo "/runner/env not present yet" >&2

/usr/bin/python3.11 /usr/local/bin/validation/precheck.py

echo "Precheck completed successfully"
