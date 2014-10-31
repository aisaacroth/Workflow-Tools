#!/bin/sh
# committer - A script that cleans a file then commits it or pushes to git.

function usage {
    echo "usage: committer [[-p push ] [-m message] [-h]]"
}

function clean_add {
    ./clean-wrap.sh $1
    git add $1
}

function commit_push {
    git commit -m "$1"
    git push
}

while [ "$1" != "" ]; do
    case $1 in
        -p | --push )
            shift
            clean_add $1
            shift
            commit_push "$1"
            ;;
        -h | --help )
            usage
            ;;
        -a | --all )
            while [ "$1" != "" ]; do
                shift
                if [ "$1" == "-m" || "$1" == "--message" ] ; then
                    break
                fi
                clean_add $1
            done
            commit_push "$2"
            ;;
    esac
    shift
done

if [ $# == 2 ] ; then
    clean_add $1
    git commit -m "$2" $1
fi
