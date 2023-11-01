SHELL := /bin/bash -O globstar

lint:
	@echo
	isort . 
	@echo
	ruff .
	@echo
	blue --check --diff --color . 
	@echo
	mypy . 
	@echo
	pip-audit

test: 
	pytest --cov-report term-missing --cov-report html --cov-branch --cov=behavioral-patterns/