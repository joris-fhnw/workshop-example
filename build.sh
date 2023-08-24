#!/usr/bin/env bash

EXERCISE_ID=94ad9af1-c38d-4a86-a13d-e584861a7144

docker build --no-cache --label=pytm.exercise="$EXERCISE_ID" -t $EXERCISE_ID .
docker stop $EXERCISE_ID && docker rm $EXERCISE_ID
docker run -p 8000:8080 -d --name $EXERCISE_ID $EXERCISE_ID:latest
