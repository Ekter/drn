#!/bin/bash

# This script is used to test the drone after a git pull. It simply launches the main.py script.

cd drn

set -e

cd src

python ~/drn/stop.py
