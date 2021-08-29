#!/bin/sh

REASON=$(python /app/main.py)
EXIT_CODE=$(echo $?)
echo "::set-output name=reason::${REASON}"
exit $EXIT_CODE