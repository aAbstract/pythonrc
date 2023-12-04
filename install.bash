#!/bin/bash

cp ./pythonrc.py $HOME/.pythonrc.py
echo 'export PYTHONSTARTUP=$HOME/.pythonrc.py' >> $HOME/.bashrc
