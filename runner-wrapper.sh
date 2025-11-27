#!/bin/sh

set -e

echo "Running Prechck Script"
/usr/local/bin/validation/precheck.sh

echo "Running the Main Playbook"
/usr/bin/ansible-runner.real "$@"
