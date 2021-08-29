#!/bin/sh

reason=$(python /app/main.py)
echo "::set-output name=reason::$reason"