#!/bin/bash
# Send a POST request to passed URL and display body response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
