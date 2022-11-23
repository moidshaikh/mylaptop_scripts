# after installing pyenv, update to latest version of python

pyenv install $(pyenv install --list | grep ' 3.*' | sed '$!d')
