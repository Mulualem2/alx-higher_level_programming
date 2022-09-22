#!/bin/bash
# Script that takes a URL and displays the HTTP
curl -sI $1 | grep -i Allow: | cut -b 8-
