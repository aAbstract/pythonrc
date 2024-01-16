#!/bin/bash

cp ./pythonrc.py $HOME/.pythonrc.py && cp -r ./pythonrc_data $HOME
echo 'export PYTHONSTARTUP=$HOME/.pythonrc.py' >> $HOME/.bashrc
