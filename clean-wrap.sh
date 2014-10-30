#!/bin/sh
python3 line_wrapper.py $1
python3 clnzr.py $1
echo "Cleaned $1"
