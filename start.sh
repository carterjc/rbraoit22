#!/bin/sh
# not for docker usage

help() {
    cat << EOF
Usage: $0 [-hd]

Run script for the RBR AOIT website Flask app

-h                      Display help

-d                      Drop databases before running

EOF
}

drop_dbs() {
    rm -f ./flaskr/database.db
}

while getopts :dh flag
do
    case "${flag}" in
        d) 
          drop_dbs
          ;;
        h | *)
          help
          exit 0
          ;;
    esac
done

gunicorn run:app
