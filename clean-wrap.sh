#!/bin/sh
function usage {
    echo "usage: clean-wrap <filename>"
}

if [ $# == 1 ] ; then
    python3 /Users/aisaacroth/Programming/Projects/Workflow-Tools/line_wrapper.py $1
    python3 /Users/aisaacroth/Programming/Projects/Workflow-Tools/clnzr.py $1
    echo "Cleaned $1"
else
    usage
fi
