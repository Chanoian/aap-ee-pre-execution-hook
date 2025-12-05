#!/usr/bin/env bash
set -e

/usr/local/bin/validation/precheck.sh "$@"

exec "$@"