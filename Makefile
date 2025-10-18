    .PHONY: venv install lint test cov run precommit
    venv:
	python -m venv .venv
    install:
	pip install -r requirements-dev.txt
    lint:
	ruff check . && black --check .
    test:
	pytest
    cov:
	pytest --cov=src --cov-report=term-missing
    precommit:
	pre-commit install
    run:
	python scripts/run_sim.py --scenario data/scenarios/sample.yaml --ticks 10 --ascii
