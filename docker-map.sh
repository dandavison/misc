# docker ps | \
#     sed 1d | \
#     while read CONTAINER_ID IMAGE COMMAND CREATED STATUS PORTS NAMES; do
#         echo "$CONTAINER_ID $IMAGE"
#         docker exec $CONTAINER_ID python3 -c 'import kruger; print(kruger.__version__)'
#         echo
#     done


docker images | \
    sed 1d | \
    while read REPOSITORY TAG IMAGE ID CREATED SIZE; do
        echo "$REPOSITORY $IMAGE"
        docker run $IMAGE python3 -c 'import kruger; print(kruger.__version__)'
        echo
    done


