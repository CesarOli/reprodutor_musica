VENV = venv-reprodutor-musica
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: run install clean

run: 
    $(PYTHON) reprodutor-musica.py
	