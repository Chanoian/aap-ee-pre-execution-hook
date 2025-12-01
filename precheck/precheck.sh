#!/usr/bin/env bash
set -e

# Only run when ansible-runner launches us
if [[ -z "$LAUNCHED_BY_RUNNER" ]]; then
    exit 0
fi

# Redirect stdout → stderr (stdout must remain JSON stream)
exec 1>&2

/usr/bin/python3 /usr/local/bin/precheck/precheck.py
exit $?

