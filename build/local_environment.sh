#!/bin/bash

root_folder=$(git rev-parse --show-toplevel)

stop_app() {
    cd $root_folder
    docker-compose down --volumes --rmi all
    printf "Environment down\n"
    printf "End at $(date +"%Y-%m-%d--%H:%M:%S")"
}

trap 'stop_app ; printf "failed for unexpected reasons"' hup int quit pipe term

start_app() {
    echo "build image and start container"
    cd $root_folder
    docker-compose up -d --force-recreate --build
    if [ $? -eq 0 ]; then
        docker image rm "$(docker image ls --filter "dangling=true" -q --no-trunc)"
        printf "Environment OK\n"
    else
        printf "Environment failed\n"
        exit 1
    fi
    printf "End at $(date +"%Y-%m-%d--%H:%M:%S")"
}

case $1 in
    start)
        start_app
    ;;
    stop)
        stop_app
    ;;
    restart)
        stop_app
        sleep 30
        start_app
    ;;
    *)
        printf "Usage: ./local_environment.sh  start/stop/restart"
        exit 1
    ;;
esac

exit 0