#!/bin/bash

# Script to build image for dev. Use Github actions for production CI/CD
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Navigate two levels up
ROOT_PATH=$(cd "$SCRIPT_DIR/../.." && pwd)

docker build -f src/mllib-recommend/Dockerfile -t mllib-recommend-app .
docker run --rm mllib-recommend-app