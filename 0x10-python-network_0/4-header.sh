#!/bin/bash
# Script that takes a URL
curl -s "$1" -X GET -H "X-School-User-Id: 98"
