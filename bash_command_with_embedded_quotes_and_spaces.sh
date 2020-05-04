#!/bin/bash

GIT_COMMITTER_NAME="FirstName LastName"

# DOCKER_RUN="docker run --env GIT_COMMITTER_NAME=\"$GIT_COMMITTER_NAME\""
# $DOCKER_RUN ubuntu env | grep GIT_COMMITTER_NAME


DOCKER_RUN_ARGS=(--env "GIT_COMMITTER_NAME=\"$GIT_COMMITTER_NAME\"")
docker run "${DOCKER_RUN_ARGS[@]}" ubuntu env | grep GIT_COMMITTER_NAME
