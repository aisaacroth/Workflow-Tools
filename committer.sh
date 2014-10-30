#!/bin/sh
./clean-wrap.sh $1
git add $1
git commit -m "$2" $1

while getopts ":a" opt; do
    case $opt in
        p)
            git push
            ;;
   esac
done
