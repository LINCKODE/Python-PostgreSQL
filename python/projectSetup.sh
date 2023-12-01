#!/usr/bin/fish
echo 'Creating Python v-env...'
python3 -m venv venv
echo 'Please activate v-env using:'
sh ./venvActivationCMD.sh
echo 'Then run ./installDeps.sh to install dependencies.'
