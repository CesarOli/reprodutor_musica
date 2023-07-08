VENV = venv-reprodutor-musica
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: run install clean

run: 
    $(PYTHON) reprodutor-musica.py

install:venv-reprodutor-musica requirements.txt
    $(PIP) install -r requirements.txt 

venv-reprodutor-musica:
    python3 -m venv $(VENV)