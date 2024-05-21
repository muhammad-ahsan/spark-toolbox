#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Navigate two levels up
ROOT_PATH=$(cd "$SCRIPT_DIR/../.." && pwd)

docker build -f src/mllib-recommend/Dockerfile -t mllib-recommend-app .
docker run --rm mllib-recommend-app