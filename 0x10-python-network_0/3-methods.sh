#!/bin/bash
# Takes in URL and displays HTTP methods sever will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
