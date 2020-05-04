# List services without using docker-compose
docker container ls -q --filter "label=com.docker.compose.service" --format '{{ .Label "com.docker.compose.service" }}'
