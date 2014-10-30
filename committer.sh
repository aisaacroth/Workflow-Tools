#!/bin/sh
while getopts ":p:" opt; do
    case $opt in
        p)
            ./clean-wrap.sh $2
            git add $2
            git commit -m "$3" $2
            git push
            ;;
    esac
done

./clean-wrap.sh $1
git add $1
git commit -m "$2" $1
