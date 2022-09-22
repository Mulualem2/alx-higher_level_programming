#!/bin/bash
# This script takes in a URL sends a request and return the size of the body of the response
curl -sI $1 | grep -i Content-Length | cut -f2 -d " "
