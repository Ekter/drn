#!/bin/bash

# This script is used to test the drone after a git pull. It simply launches the main.py script.

cd drn
git pull

set -e
sudo pigpiod

source .venv/bin/activate

cd src

python main.py
