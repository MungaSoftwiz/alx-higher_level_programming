#!/bin/bash
# Get byte size of HTTP response header for an URL
curl -s "$1" | wc -c
