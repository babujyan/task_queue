PROJECT = queue
PYTHON_VERSION=3.12
venv_name = ${PROJECT}-py${PYTHON_VERSION}
venv = .venv/${venv_name}

export DEVELOPMENT=false

.PHONY: default default install_deps setup_git_hooks test lint format
default: ${venv} setup_git_hooks


${venv}: requirements.txt
	python${PYTHON_VERSION} -m venv ${venv}
	. ${venv}/bin/activate; pip install --upgrade pip Cython==0.28 --cache .tmp/
	. ${venv}/bin/activate; pip install -r requirements.txt --cache .tmp/
	@echo Success, to activate the development environment, run:
	@echo "\tsource .venv/${venv_name}/bin/activate"

install_deps:
	pip install --upgrade --force-reinstall -r requirements.txt

setup_git_hooks:
	@echo '#!/bin/sh\nmake lint test' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

test:
	. ${venv}/bin/activate; python -m unittest discover -s tests

lint:
	. ${venv}/bin/activate; black --check .

format:
	. ${venv}/bin/activate; black .
