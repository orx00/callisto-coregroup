.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

TOX_REQUIREMENTS := requirements/test.txt requirements.txt

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc clean-tox

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-tox:
	rm -f tox.ini

lint: ## check style with flake8 and isort
	flake8 callisto/
	isort --check-only --diff --quiet -rc callisto/

clean-lint:
	isort -rc callisto/
	autopep8 --in-place --recursive --aggressive --aggressive callisto/ --max-line-length 119 --exclude="*/migrations/*"

test: ## run tests quickly with the default Python
	python runtests.py tests

test-all: ## run tests on every Python version with tox
	tox

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/callisto-core.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ callisto
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

sdist: clean ## package
	python setup.py sdist
	ls -l dist
