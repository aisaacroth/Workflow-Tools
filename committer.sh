#!/bin/sh
# committer = A script that cleans a file then commits it or pushes to git.

function usage {
    echo "usage: committer [[-p push ] [-h]]"
}

while [ "$1" != "" ]; do
    case $1 in
        -p | --push )
            shift
            ./clean-wrap.sh $1
            git add $1
            shift
            git commit -m "$1"
            git push
            ;;
        -h | --help )
            usage
            ;;
        -a | --all )
            while [ "$1" != "" ]; do
                shift
                echo "$1"
                if [ "$1" == "-c" ] ; then
                    break
                fi
                ./clean-wrap.sh $1
                git add $1
            done
            git commit -m "$2"
            ;;
    esac
    shift
done

if [ $# == 2 ] ; then
    ./clean-wrap.sh $1
    git add $1
    git commit -m "$2" $1
fi
