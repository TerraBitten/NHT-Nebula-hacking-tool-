#!/bin/sh

echo "Installing Required Dependecies. . ."
sudo apt update
sudo apt install python3-pip -y
pip install subprocess webbrowser random requests time
GREEN="\033[32m"
RESET="\033[0m"

MESSAGE="	Required Packages Installed "
MESSAGE2="	You now can run ./run.sh "
echo -e "${GREEN}${MESSAGE}${MESSAGE2}${RESET}"

