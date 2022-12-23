#!/bin/bash

brew install pyenv pipx
pyenv install 3.10.1
pyenv local 3.10.1
pipx ensurepath
path=${which python}
pipx install --python $path txsweeper
pyenv local system

echo Done!
