#!/bin/bash

brew install pyenv pipx
pyenv install 3.10.1
pyenv local 3.10.1
pipx ensurepath
pipx install --python ${which python} txsweeper
pyenv local system

echo Done!
