#!/bin/bash
set -e

# Script to build image for dev. Use Github actions for production CI/CD
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Navigate one levels up
ROOT_PATH=$(cd "$SCRIPT_DIR/.." && pwd)
cd $ROOT_PATH

# Add new apps here
VALID_OPTIONS=("mllib-recommend" "pi" "sum" "word-count")

# Function to check if the provided app name is valid
is_valid_option() {
    local input=$1
    for option in "${VALID_OPTIONS[@]}"; do
        if [[ "$option" == "$input" ]]; then
            return 0
        fi
    done
    return 1
}

# Prompt the user until a valid option is provided
while true; do
    echo "Available spark apps are:"
    for option in "${VALID_OPTIONS[@]}"; do
        echo " - $option"
    done
    read -p "Enter name of spark app: " app_name
    if is_valid_option "$app_name"; then
        break
    else
        echo "Invalid option. Please try again."
    fi
done

echo "Going to execute app -> $app_name"

dockerfile_path="src/$app_name/Dockerfile"
echo $dockerfile_path
docker build -f $dockerfile_path -t "mahsan/$app_name" .
docker push "mahsan/$app_name"

# To run the app
# docker run --rm "mahsan/$app_name"